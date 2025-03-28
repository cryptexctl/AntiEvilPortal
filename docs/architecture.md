# Архитектура

## Общая структура

```
AntiEvilPortal/
├── AntiEvilPortal.py    # Основной файл приложения
├── network.py           # Модуль работы с сетью
├── attacker.py          # Модуль атак
├── ui.py               # Модуль интерфейса
├── config.py           # Конфигурационный модуль
├── requirements.txt    # Зависимости
└── docs/              # Документация
    ├── README.md
    ├── overview.md
    ├── architecture.md
    ├── setup.md
    ├── usage.md
    ├── api.md
    ├── security.md
    └── troubleshooting.md
```

## Компоненты системы

### NetworkManager (network.py)

Отвечает за:
- Сканирование WiFi сетей
- Подключение к сетям
- Отправку HTTP запросов
- Генерацию payload

### EvilPortalAttacker (attacker.py)

Отвечает за:
- Реализацию методов атак
- Управление потоками
- Обработку результатов

### ScannerUI (ui.py)

Отвечает за:
- Графический интерфейс
- Отображение логов
- Управление прогрессом
- Обработку пользовательского ввода

### Конфигурация (config.py)

Содержит:
- Настройки сети
- Параметры атак
- Настройки UI
- Пути к файлам

## Взаимодействие компонентов

1. Пользователь запускает приложение
2. UI инициализирует NetworkManager и EvilPortalAttacker
3. При нажатии "Сканировать":
   - NetworkManager сканирует сети
   - EvilPortalAttacker анализирует результаты
   - UI отображает прогресс и результаты
4. При обнаружении Evil Portal:
   - EvilPortalAttacker запускает атаку
   - NetworkManager отправляет запросы
   - UI показывает статус атаки 