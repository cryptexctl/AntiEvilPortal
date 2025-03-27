import logging
from network import NetworkManager
from config import *

class EvilPortalAttacker:
    def __init__(self):
        self.logger = logging.getLogger("attacker")
        self.network = NetworkManager()

    def scan(self):
        results = self.network.scan_networks()
        ssids = []
        for result in results:
            if self.network.is_evil_portal(result):
                ssids.append(result.ssid)
        return ssids

    def attack(self, ssid: str, progress_var):
        self.logger.info(f"Подключаемся к сети: {ssid}")
        if not self.network.connect_to_network(ssid):
            self.logger.error("Не удалось подключиться к сети")
            return

        progress_var.set(0.2)

        # Проверка типичных адресов ESP
        possible_hosts = ["http://172.0.0.1", "http://192.168.4.1"]
        host = None

        for h in possible_hosts:
            try:
                self.network.send_request(h, method="GET")
                host = h
                self.logger.info(f"Найден Evil Portal по адресу: {host}")
                break
            except Exception as e:
                self.logger.warning(f"Адрес {h} не ответил: {str(e)}")

        if not host:
            self.logger.warning("Не удалось найти портал по стандартным адресам")
            return

        progress_var.set(0.4)

        try:
            self.logger.info("Атака CREDS...")
            self.network.send_request(host, method="POST", payload={
                "username": self.network.generate_random_string(),
                "password": self.network.generate_random_string()
            })
        except Exception as e:
            self.logger.error(f"Ошибка в CREDS методе: {str(e)}")

        progress_var.set(0.6)

        try:
            self.logger.info("Атака FORM...")
            self.network.send_request(host, method="POST", payload={
                "form": self.network.generate_payload()
            })
        except Exception as e:
            self.logger.error(f"Ошибка в FORM методе: {str(e)}")

        progress_var.set(0.8)

        try:
            self.logger.info("Атака FETCH...")
            self.network.send_request(host, method="POST", payload={
                "fetch": self.network.generate_payload()
            })
        except Exception as e:
            self.logger.error(f"Ошибка в FETCH методе: {str(e)}")

        try:
            self.logger.info("Атака XMLHttpRequest...")
            self.network.send_request(host, method="POST", payload={
                "xhr": self.network.generate_payload()
            })
        except Exception as e:
            self.logger.error(f"Ошибка в XMLHttpRequest методе: {str(e)}")

        progress_var.set(1.0)
        self.logger.info("Атака завершена")