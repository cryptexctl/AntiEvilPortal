# Установка и настройка

## Требования к системе

- Python 3.7 или выше
- WiFi адаптер с поддержкой мониторинга
- Операционная система: Windows/Linux/macOS
- Права администратора для работы с WiFi

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/AntiEvilPortal.git
cd AntiEvilPortal
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Настройка

1. Создайте файл `.env` в корневой директории проекта:
```env
PAYLOAD_SIZE=100000
SCAN_INTERVAL=3
CONNECTION_TIMEOUT=5
MAX_RETRIES=100
THREAD_COUNT=5
PAYLOAD_CHUNK_SIZE=64
RANDOM_STRING_LENGTH=6
```

2. Настройте права доступа к WiFi адаптеру:
   - Windows: Запустите программу от имени администратора
   - Linux: Добавьте пользователя в группу netdev
   - macOS: Предоставьте доступ к WiFi в настройках безопасности

## Проверка установки

1. Запустите программу:
```bash
python AntiEvilPortal.py
```

2. Нажмите кнопку "Сканировать"

3. Проверьте, что:
   - Программа запускается без ошибок
   - Отображается список доступных сетей
   - Работает прогресс-бар
   - Создаются логи в файле scanner.log 