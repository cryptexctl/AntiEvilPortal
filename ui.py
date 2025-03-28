import customtkinter as ctk
import logging
from typing import Callable
from config import *

class ScannerUI:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry(WINDOW_SIZE)
        
        self.setup_logging()
        self.setup_ui()
        
    def setup_logging(self):
        """Настраивает логирование"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(LOG_FILE),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def setup_ui(self):
        """Настраивает пользовательский интерфейс"""
        # Создаем фрейм для логов
        log_frame = ctk.CTkFrame(self.window)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # Создаем текстовое поле для логов
        self.log_text = ctk.CTkTextbox(log_frame, state='disabled')
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)

        # Создаем фрейм для кнопок
        button_frame = ctk.CTkFrame(self.window)
        button_frame.pack(fill="x", padx=10, pady=5)

        # Создаем кнопки
        self.scan_button = ctk.CTkButton(
            button_frame,
            text="Сканировать",
            command=self.start_scan
        )
        self.scan_button.pack(side="left", padx=5)

        self.clear_button = ctk.CTkButton(
            button_frame,
            text="Очистить",
            command=self.clear_logs
        )
        self.clear_button.pack(side="left", padx=5)

        # Создаем прогресс-бар
        self.progress_bar = ctk.CTkProgressBar(self.window)
        self.progress_bar.pack(fill="x", padx=10, pady=5)
        self.progress_bar.set(0)

    def add_log(self, text: str):
        """Добавляет текст в лог"""
        self.log_text.configure(state='normal')
        self.log_text.insert("end", text + "\n")
        self.log_text.see("end")
        self.log_text.configure(state='disabled')
        self.logger.info(text)

    def clear_logs(self):
        """Очищает логи"""
        self.log_text.configure(state='normal')
        self.log_text.delete("0.0", "end")
        self.log_text.configure(state='disabled')
        self.logger.info("Логи очищены")

    def update_progress(self, value: float):
        """Обновляет прогресс-бар"""
        self.progress_bar.set(value)

    def start_scan(self):
        """Запускает сканирование"""
        self.scan_button.configure(state='disabled')
        self.clear_logs()
        self.update_progress(0)
        # Здесь будет логика сканирования

    def run(self):
        """Запускает приложение"""
        self.window.mainloop() 