import tkinter as tk
import customtkinter as ctk
from attacker import EvilPortalAttacker

class ScannerUI:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("AntiEvilPortal")
        self.root.geometry("600x500")

        self.attacker = EvilPortalAttacker()

        self.network_list = []
        self.selected_network = tk.StringVar()
        self.progress_var = tk.DoubleVar()

        self.setup_ui()

    def setup_ui(self):
        self.label = ctk.CTkLabel(self.root, text="Выберите Wi-Fi сеть:")
        self.label.pack(pady=10)

        self.dropdown = ctk.CTkOptionMenu(self.root, variable=self.selected_network, values=self.network_list)
        self.dropdown.pack(pady=10)

        self.scan_button = ctk.CTkButton(self.root, text="Сканировать", command=self.scan_networks)
        self.scan_button.pack(pady=10)

        self.attack_button = ctk.CTkButton(self.root, text="Атаковать", command=self.attack_network)
        self.attack_button.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self.root, variable=self.progress_var)
        self.progress.pack(pady=20)
        self.progress.set(0)

        self.log_box = ctk.CTkTextbox(self.root, width=500, height=200)
        self.log_box.pack(pady=10)

    def scan_networks(self):
        self.add_log("Сканируем сети...")
        self.progress_var.set(0.2)
        self.root.update()

        self.network_list = self.attacker.scan()
        if self.network_list:
            self.selected_network.set(self.network_list[0])
            self.dropdown.configure(values=self.network_list)
            self.add_log(f"Найдено сетей: {len(self.network_list)}")
        else:
            self.selected_network.set("")
            self.add_log("Сети не найдены.")

        self.progress_var.set(1)

    def attack_network(self):
        ssid = self.selected_network.get()
        if ssid:
            self.add_log(f"Атакуем сеть: {ssid}")
            self.attacker.attack(ssid, self.progress_var)
        else:
            self.add_log("Сеть не выбрана.")

    def add_log(self, message: str):
        self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)

    def update_progress(self, value: float):
        self.progress_var.set(value)
        self.root.update()

    def run(self):
        self.root.mainloop()