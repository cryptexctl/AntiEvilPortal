# NetworkManager

## Описание

NetworkManager - это модуль, отвечающий за работу с WiFi сетями. Он обеспечивает:
- Сканирование доступных сетей
- Подключение к сетям
- Отправку HTTP запросов
- Генерацию payload для атак

## Основные функции

### Инициализация
```python
def __init__(self):
    self.wifi = pywifi.PyWiFi()
    self.iface = self.wifi.interfaces()[0]
    self.logger = logging.getLogger(__name__)
```

### Генерация payload
```python
def generate_payload(self) -> str:
    return 'vorobushek' * (PAYLOAD_SIZE // 10)
```

### Создание профиля WiFi
```python
def create_profile(self, ssid: str) -> pywifi.Profile:
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = pywifi.const.AUTH_ALG_OPEN
    profile.akm.append(pywifi.const.AKM_TYPE_NONE)
    profile.cipher = pywifi.const.AKM_TYPE_NONE
    profile.key = ''
    return profile
```

### Подключение к сети
```python
def connect_to_network(self, ssid: str) -> bool:
    try:
        self.iface.disconnect()
        profile = self.create_profile(ssid)
        self.iface.connect(self.iface.add_network_profile(profile))
        return True
    except Exception as e:
        self.logger.error(f"Ошибка подключения к сети {ssid}: {str(e)}")
        return False
```

### Сканирование сетей
```python
def scan_networks(self) -> List[pywifi.ScanResult]:
    try:
        self.iface.scan()
        return self.iface.scan_results()
    except Exception as e:
        self.logger.error(f"Ошибка сканирования сетей: {str(e)}")
        return []
```

### Проверка на Evil Portal
```python
def is_evil_portal(self, result: pywifi.ScanResult) -> bool:
    return (result.akm == [pywifi.const.AKM_TYPE_NONE] and 
            result.cipher == pywifi.const.AKM_TYPE_NONE and 
            result.ssid.strip() != '')
```

### Отправка HTTP запросов
```python
def send_request(self, url: str, method: str = 'GET', payload: dict = None) -> requests.Response:
    headers = {
        'user-agent': self.generate_payload(),
        'cookie': self.generate_payload(),
        'accept': self.generate_payload(),
        'accept-encoding': self.generate_payload(),
        'accept-language': self.generate_payload()
    }
    
    try:
        if method.upper() == 'GET':
            return requests.get(url, params=payload, headers=headers, timeout=CONNECTION_TIMEOUT)
        else:
            return requests.post(url, json=payload, headers=headers, timeout=CONNECTION_TIMEOUT)
    except requests.RequestException as e:
        self.logger.error(f"Ошибка отправки запроса: {str(e)}")
        raise
```

## Использование

```python
# Создание экземпляра
network_manager = NetworkManager()

# Сканирование сетей
networks = network_manager.scan_networks()

# Проверка сети
for network in networks:
    if network_manager.is_evil_portal(network):
        # Подключение к сети
        if network_manager.connect_to_network(network.ssid):
            # Отправка запроса
            response = network_manager.send_request('http://example.com')
```

## Обработка ошибок

Модуль обрабатывает следующие типы ошибок:
- Ошибки подключения к сети
- Ошибки сканирования
- Ошибки HTTP запросов
- Ошибки создания профиля

Все ошибки логируются и обрабатываются на уровне модуля. 