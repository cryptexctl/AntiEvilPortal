import tkinter as tk
from tkinter import ttk, scrolledtext
import logging
from typing import Optional
from network import NetworkManager
from attacker import EvilPortalAttacker
from config import *

class ScannerUI:
    def __init__(self):
        self.progress_var = tk.DoubleVar()
        self.progress_var.set(0)
        
        self.root = tk.Tk()
        self.root.title("AntiEvilPortal Scanner")
        self.root.geometry("800x600")
        
        self.network_manager = NetworkManager()
        self.attacker = EvilPortalAttacker()
        
        self.setup_logging()
        self.setup_ui()
        
        self.scanning = False
        self.current_network = None

    def setup_logging(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        handler = logging.StreamHandler()
        handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)

    def setup_ui(self):
        self.log_text = scrolledtext.ScrolledText(self.root, height=20)
        self.log_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.progress_bar = ttk.Progressbar(
            self.root,
            variable=self.progress_var,
            maximum=100
        )
        self.progress_bar.pack(padx=10, pady=5, fill=tk.X)
        
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=5)
        
        self.scan_button = ttk.Button(
            button_frame,
            text="Начать сканирование",
            command=self.start_scan
        )
        self.scan_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_button = ttk.Button(
            button_frame,
            text="Очистить логи",
            command=self.clear_logs
        )
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def add_log(self, message: str):
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)

    def clear_logs(self):
        self.log_text.delete(1.0, tk.END)
        self.progress_var.set(0)

    def update_progress(self, value: float):
        self.progress_var.set(value)
        self.root.update_idletasks()

    def start_scan(self):
        if self.scanning:
            return
            
        self.scanning = True
        self.scan_button.config(state=tk.DISABLED)
        self.clear_logs()
        
        try:
            networks = self.network_manager.scan_networks()
            total_networks = len(networks)
            
            for i, network in enumerate(networks):
                self.current_network = network
                self.add_log(f"Сканирование сети: {network}")
                self.update_progress((i + 1) / total_networks * 100)
                
                if self.network_manager.is_evil_portal(network):
                    self.add_log(f"Обнаружен Evil Portal: {network}")
                    if self.attacker.attack_network(network, "http://192.168.4.1"):
                        self.add_log(f"Успешная атака на сеть: {network}")
                    else:
                        self.add_log(f"Не удалось атаковать сеть: {network}")
                else:
                    self.add_log(f"Сеть {network} не является Evil Portal")
                    
        except Exception as e:
            self.add_log(f"Ошибка при сканировании: {str(e)}")
        finally:
            self.scanning = False
            self.scan_button.config(state=tk.NORMAL)
            self.update_progress(100)

    def run(self):
        self.root.mainloop() 