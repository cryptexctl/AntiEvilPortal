# Конфигурация

## Общее описание

Конфигурация приложения находится в файле `config.py` и управляется через переменные окружения с помощью python-dotenv.

## Структура конфигурации

### Настройки сети
```python
# Размер payload в байтах
PAYLOAD_SIZE = 100000

# Интервал сканирования в секундах
SCAN_INTERVAL = 3

# Таймаут подключения в секундах
CONNECTION_TIMEOUT = 5

# Максимальное количество попыток
MAX_RETRIES = 100
```

### Настройки атак
```python
# Количество потоков для атаки
THREAD_COUNT = 5

# Размер чанка payload
PAYLOAD_CHUNK_SIZE = 64

# Длина случайной строки
RANDOM_STRING_LENGTH = 6
```

### Настройки UI
```python
# Размер окна
WINDOW_SIZE = "500x500"

# Заголовок окна
WINDOW_TITLE = "Anti Evil Portal Scanner"
```

### Пути для логов
```python
# Файл логов
LOG_FILE = "scanner.log"
```

## Переменные окружения

Создайте файл `.env` в корневой директории проекта:

```env
# Настройки сети
PAYLOAD_SIZE=100000
SCAN_INTERVAL=3
CONNECTION_TIMEOUT=5
MAX_RETRIES=100

# Настройки атак
THREAD_COUNT=5
PAYLOAD_CHUNK_SIZE=64
RANDOM_STRING_LENGTH=6

# Настройки UI
WINDOW_SIZE=500x500
WINDOW_TITLE=Anti Evil Portal Scanner

# Пути для логов
LOG_FILE=scanner.log
```

## Использование

1. **Импорт конфигурации**
```python
from config import *
```

2. **Использование переменных**
```python
# В NetworkManager
payload = 'vorobushek' * (PAYLOAD_SIZE // 10)

# В EvilPortalAttacker
threads = []
for _ in range(THREAD_COUNT):
    thread = threading.Thread(target=self._attack_thread, args=(ssid, action))
    threads.append(thread)

# В ScannerUI
self.window.geometry(WINDOW_SIZE)
self.window.title(WINDOW_TITLE)
```

## Изменение конфигурации

1. **Через файл .env**
   - Отредактируйте значения в файле
   - Перезапустите приложение

2. **Через переменные окружения**
```bash
export PAYLOAD_SIZE=200000
export THREAD_COUNT=10
python AntiEvilPortal.py
```

3. **Через код**
   - Измените значения в config.py
   - Перезапустите приложение

## Безопасность

- Не храните чувствительные данные в конфигурации
- Используйте переменные окружения для секретов
- Проверяйте значения перед использованием
- Логируйте изменения конфигурации 