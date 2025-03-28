import pywifi
import requests
import random
import string
import logging
import time
from typing import List, Tuple
from config import *

class NetworkManager:
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]
        self.logger = logging.getLogger(__name__)
        self.portal_ips = ['172.0.0.1', '192.168.4.1']
        self.portal_check_timeout = 10
        self.portal_ports = ['80', '443']  # Добавляем порты для проверки

    def generate_payload(self) -> str:
        return 'vorobushek' * (PAYLOAD_SIZE // 10)

    def generate_random_string(self, length: int = RANDOM_STRING_LENGTH) -> str:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def create_profile(self, ssid: str) -> pywifi.Profile:
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_NONE)
        profile.cipher = pywifi.const.AKM_TYPE_NONE
        profile.key = ''
        return profile

    def connect_to_network(self, ssid: str) -> bool:
        try:
            self.iface.disconnect()
            profile = self.create_profile(ssid)
            self.iface.connect(self.iface.add_network_profile(profile))
            time.sleep(2)
            return True
        except Exception as e:
            self.logger.error(f"Ошибка подключения к сети {ssid}: {str(e)}")
            return False

    def scan_networks(self) -> List[object]:
        try:
            self.iface.scan()
            return self.iface.scan_results()
        except Exception as e:
            self.logger.error(f"Ошибка сканирования сетей: {str(e)}")
            return []

    def is_evil_portal(self, result: object) -> bool:
        return (result.akm == [pywifi.const.AKM_TYPE_NONE] and 
                result.cipher == pywifi.const.AKM_TYPE_NONE and 
                result.ssid.strip() != '')

    def check_portal_ip(self, ssid: str) -> str:
        for ip in self.portal_ips:
            for port in self.portal_ports:
                try:
                    protocol = 'https' if port == '443' else 'http'
                    url = f'{protocol}://{ip}:{port}/'
                    self.logger.info(f'Проверяем {protocol}://{ip}:{port}')
                    
                    # Для HTTPS отключаем проверку сертификата
                    verify = False if protocol == 'https' else True
                    response = requests.get(url, timeout=self.portal_check_timeout, verify=verify)
                    
                    if "<div class=form-container>" in response.text:
                        self.logger.info(f'Найден Evil Portal на {protocol}://{ip}:{port}')
                        return url
                    time.sleep(1)
                except requests.Timeout:
                    self.logger.info(f'Таймаут при проверке {protocol}://{ip}:{port}')
                    continue
                except requests.ConnectionError:
                    self.logger.info(f'Ошибка подключения к {protocol}://{ip}:{port}')
                    continue
                except requests.exceptions.SSLError:
                    self.logger.info(f'Ошибка SSL при проверке {protocol}://{ip}:{port}')
                    continue
                except Exception as e:
                    self.logger.error(f'Ошибка при проверке {protocol}://{ip}:{port}: {str(e)}')
                    continue
        return None

    def send_request(self, url: str, method: str = 'GET', payload: dict = None) -> requests.Response:
        headers = {
            'user-agent': self.generate_payload(),
            'cookie': self.generate_payload(),
            'accept': self.generate_payload(),
            'accept-encoding': self.generate_payload(),
            'accept-language': self.generate_payload()
        }
        
        try:
            verify = False if url.startswith('https') else True
            if method.upper() == 'GET':
                return requests.get(url, params=payload, headers=headers, timeout=CONNECTION_TIMEOUT, verify=verify)
            else:
                return requests.post(url, json=payload, headers=headers, timeout=CONNECTION_TIMEOUT, verify=verify)
        except requests.RequestException as e:
            self.logger.error(f"Ошибка отправки запроса: {str(e)}")
            raise 