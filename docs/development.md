# Разработка

## Требования к разработке

### 1. Python
- Версия: 3.7+
- Типизация: используйте type hints
- Стиль: PEP 8
- Документация: docstrings

### 2. Зависимости
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # для разработки
```

### 3. Инструменты
- Git для контроля версий
- pytest для тестирования
- black для форматирования
- pylint для проверки кода
- mypy для проверки типов

## Структура проекта

```
AntiEvilPortal/
├── AntiEvilPortal.py    # Основной файл
├── network.py           # Модуль сети
├── attacker.py          # Модуль атак
├── ui.py               # Модуль UI
├── config.py           # Конфигурация
├── requirements.txt    # Зависимости
├── requirements-dev.txt # Зависимости для разработки
├── tests/             # Тесты
├── docs/              # Документация
└── .env              # Переменные окружения
```

## Разработка модулей

### 1. NetworkManager
```python
class NetworkManager:
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]
        self.logger = logging.getLogger(__name__)

    def scan_networks(self) -> List[pywifi.ScanResult]:
        try:
            self.iface.scan()
            return self.iface.scan_results()
        except Exception as e:
            self.logger.error(f"Ошибка сканирования: {str(e)}")
            return []
```

### 2. EvilPortalAttacker
```python
class EvilPortalAttacker:
    def __init__(self):
        self.network_manager = NetworkManager()
        self.logger = logging.getLogger(__name__)
        self.attack_successful = False

    def attack_network(self, ssid: str, url: str) -> bool:
        self.attack_successful = False
        if not self.network_manager.connect_to_network(ssid):
            return False
        # ... код атаки ...
```

### 3. ScannerUI
```python
class ScannerUI:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry(WINDOW_SIZE)
        self.setup_logging()
        self.setup_ui()
```

## Тестирование

### 1. Unit тесты
```python
def test_network_manager():
    manager = NetworkManager()
    networks = manager.scan_networks()
    assert isinstance(networks, list)

def test_evil_portal_detection():
    manager = NetworkManager()
    result = pywifi.ScanResult()
    result.ssid = "test"
    result.akm = [pywifi.const.AKM_TYPE_NONE]
    result.cipher = pywifi.const.AKM_TYPE_NONE
    assert manager.is_evil_portal(result)
```

### 2. Интеграционные тесты
```python
def test_full_scan():
    app = AntiEvilPortal()
    app.scan_networks()
    assert app.ui.log_text.get("1.0", "end-1c") != ""
```

## Отладка

### 1. Логирование
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### 2. Отладчик
```python
import pdb

def some_function():
    pdb.set_trace()  # точка остановки
    # код
```

## Стиль кода

### 1. Форматирование
```bash
# Установка black
pip install black

# Форматирование кода
black .
```

### 2. Проверка типов
```bash
# Установка mypy
pip install mypy

# Проверка типов
mypy .
```

### 3. Линтер
```bash
# Установка pylint
pip install pylint

# Проверка кода
pylint .
```

## Git

### 1. Ветки
- main: основной код
- develop: разработка
- feature/*: новые функции
- bugfix/*: исправления
- release/*: релизы

### 2. Коммиты
```
feat: добавлена новая функция
fix: исправлена ошибка
docs: обновлена документация
style: форматирование кода
refactor: рефакторинг
test: добавлены тесты
chore: обновление зависимостей
```

### 3. Pull Request
1. Создайте ветку
2. Внесите изменения
3. Напишите тесты
4. Обновите документацию
5. Создайте PR
6. Пройдите проверки
7. Получите ревью
8. Смержите изменения

## Релиз

### 1. Подготовка
- Обновите версию
- Проверьте зависимости
- Запустите тесты
- Обновите документацию

### 2. Сборка
```bash
# Создание пакета
python setup.py sdist bdist_wheel

# Загрузка в PyPI
twine upload dist/*
```

### 3. Документация
- Обновите README.md
- Обновите CHANGELOG.md
- Создайте релиз на GitHub 