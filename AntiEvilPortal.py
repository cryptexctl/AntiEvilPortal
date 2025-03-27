import threading
import logging
from ui import ScannerUI
from network import NetworkManager
from attacker import EvilPortalAttacker
from config import *

class AntiEvilPortal:
    def __init__(self):
        self.ui = ScannerUI()
        self.network_manager = NetworkManager()
        self.attacker = EvilPortalAttacker()
        self.logger = logging.getLogger(__name__)

    def scan_networks(self):
        """Сканирует сети на наличие Evil Portal"""
        try:
            self.ui.add_log('Проверяем сети на наличие Evil Portal...')
            networks = self.network_manager.scan_networks()
            
            if not networks:
                self.ui.add_log('Не найдено доступных сетей')
                return

            total_networks = len(networks)
            evil_portals = []

            for i, network in enumerate(networks):
                self.ui.update_progress(i / total_networks)
                
                if self.network_manager.is_evil_portal(network):
                    self.ui.add_log(f'Найдена потенциальная Evil Portal сеть: {network.ssid}')
                    evil_portals.append(network)

            if evil_portals:
                self.ui.add_log(f'\nНайдено {len(evil_portals)} Evil Portal сетей:')
                for network in evil_portals:
                    self.ui.add_log(f'- {network.ssid}')
                
                # Запускаем атаку на каждую найденную сеть
                for network in evil_portals:
                    self.attack_network(network.ssid)
            else:
                self.ui.add_log('Evil Portal сети не найдены')

        except Exception as e:
            self.logger.error(f"Ошибка при сканировании: {str(e)}")
            self.ui.add_log(f'Ошибка: {str(e)}')
        finally:
            self.ui.scan_button.configure(state='normal')
            self.ui.update_progress(1)

    def attack_network(self, ssid: str):
        """Атакует Evil Portal сеть"""
        try:
            self.ui.add_log(f'\nАтакуем сеть {ssid}...')
            url = f'http://{ssid}/'
            
            if self.attacker.attack(ssid, url):
                self.ui.add_log(f'Сеть {ssid} успешно атакована!')
            else:
                self.ui.add_log(f'Не удалось атаковать сеть {ssid}')
                
        except Exception as e:
            self.logger.error(f"Ошибка при атаке сети {ssid}: {str(e)}")
            self.ui.add_log(f'Ошибка: {str(e)}')

    def run(self):
        """Запускает приложение"""
        self.ui.scan_button.configure(command=self.scan_networks)
        self.ui.run()

if __name__ == '__main__':
    app = AntiEvilPortal()
    app.run()