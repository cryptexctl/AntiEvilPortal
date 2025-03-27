import os
from dotenv import load_dotenv

load_dotenv()

# Настройки сети
PAYLOAD_SIZE = 100000  # Размер payload в байтах
SCAN_INTERVAL = 3  # Интервал сканирования в секундах
CONNECTION_TIMEOUT = 5  # Таймаут подключения в секундах
MAX_RETRIES = 100  # Максимальное количество попыток

# Настройки атаки
THREAD_COUNT = 5  # Количество потоков для атаки
PAYLOAD_CHUNK_SIZE = 64  # Размер чанка payload
RANDOM_STRING_LENGTH = 6  # Длина случайной строки

# Настройки UI
WINDOW_SIZE = "500x500"
WINDOW_TITLE = "Anti Evil Portal Scanner"

# Пути для логов
LOG_FILE = "scanner.log" 