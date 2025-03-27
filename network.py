import logging
import pywifi
import requests
import random
import string
from typing import List
from config import *

class NetworkManager:
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]
        self.logger = logging.getLogger("network")

    def generate_payload(self) -> str:
        return 'vorobushek' * (PAYLOAD_SIZE // 10)

    def generate_random_string(self, length: int = RANDOM_STRING_LENGTH) -> str:
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

    def create_profile(self, ssid: str):
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_NONE)
        profile.cipher = pywifi.const.CIPHER_TYPE_NONE
        profile.key = ''
        return profile

    def connect_to_network(self, ssid: str) -> bool:
        try:
            self.iface.disconnect()
            profile = self.create_profile(ssid)
            self.iface.remove_all_network_profiles()
            tmp_profile = self.iface.add_network_profile(profile)
            self.iface.connect(tmp_profile)
            return True
        except Exception as e:
            self.logger.error(f"Ошибка подключения к сети {ssid}: {str(e)}")
            return False

    def scan_networks(self) -> List:
        try:
            self.iface.scan()
            return self.iface.scan_results()
        except Exception as e:
            self.logger.error(f"Ошибка сканирования сетей: {str(e)}")
            return []

    def is_evil_portal(self, result) -> bool:
        return (result.akm == [pywifi.const.AKM_TYPE_NONE] and 
                result.cipher == pywifi.const.CIPHER_TYPE_NONE and 
                result.ssid.strip() != '')

    def send_request(self, url: str, method: str = 'GET', payload: dict = None) -> requests.Response:
        headers = {
            'user-agent': self.generate_payload(),
            'cookie': self.generate_payload(),
            'accept': self.generate_payload(),
            'accept-encoding': self.generate_payload(),
            'accept-language': self.generate_payload()
        }

        try:
            if method.upper() == 'GET':
                return requests.get(url, params=payload, headers=headers, timeout=CONNECTION_TIMEOUT)
            else:
                return requests.post(url, json=payload, headers=headers, timeout=CONNECTION_TIMEOUT)
        except requests.RequestException as e:
            self.logger.error(f"Ошибка отправки запроса: {str(e)}")
            raise

    def try_evil_endpoints(self) -> str:
        possible_hosts = ["http://172.0.0.1", "http://192.168.4.1"]
        for host in possible_hosts:
            try:
                resp = self.send_request(host)
                if resp.status_code == 200:
                    self.logger.info(f"Evil Portal найден по адресу: {host}")
                    return host
            except Exception:
                continue
        return ""