# API Документация

## NetworkManager

### Методы

#### generate_payload()
```python
def generate_payload(self) -> str
```
Генерирует payload для атаки.

#### generate_random_string(length: int = RANDOM_STRING_LENGTH)
```python
def generate_random_string(self, length: int = RANDOM_STRING_LENGTH) -> str
```
Генерирует случайную строку заданной длины.

#### create_profile(ssid: str)
```python
def create_profile(self, ssid: str) -> pywifi.Profile
```
Создает профиль WiFi для подключения.

#### connect_to_network(ssid: str)
```python
def connect_to_network(self, ssid: str) -> bool
```
Подключается к указанной сети.

#### scan_networks()
```python
def scan_networks(self) -> List[pywifi.ScanResult]
```
Сканирует доступные сети.

#### is_evil_portal(result: pywifi.ScanResult)
```python
def is_evil_portal(self, result: pywifi.ScanResult) -> bool
```
Проверяет, является ли сеть Evil Portal.

#### send_request(url: str, method: str = 'GET', payload: dict = None)
```python
def send_request(self, url: str, method: str = 'GET', payload: dict = None) -> requests.Response
```
Отправляет HTTP запрос.

## EvilPortalAttacker

### Методы

#### attack_network(ssid: str, url: str)
```python
def attack_network(self, ssid: str, url: str) -> bool
```
Атакует указанную сеть.

#### _attack_ssid_method(ssid: str, url: str)
```python
def _attack_ssid_method(self, ssid: str, url: str) -> bool
```
Атака через SSID метод.

#### _attack_creds_method(ssid: str, url: str)
```python
def _attack_creds_method(self, ssid: str, url: str) -> bool
```
Атака через CREDS метод.

#### _attack_form_method(ssid: str, url: str)
```python
def _attack_form_method(self, ssid: str, url: str) -> bool
```
Атака через FORM метод.

#### _attack_fetch_method(ssid: str, url: str)
```python
def _attack_fetch_method(self, ssid: str, url: str) -> bool
```
Атака через FETCH метод.

#### _attack_xmlhttp_method(ssid: str, url: str)
```python
def _attack_xmlhttp_method(self, ssid: str, url: str) -> bool
```
Атака через XMLHttpRequest метод.

## ScannerUI

### Методы

#### add_log(text: str)
```python
def add_log(self, text: str)
```
Добавляет текст в лог.

#### clear_logs()
```python
def clear_logs(self)
```
Очищает логи.

#### update_progress(value: float)
```python
def update_progress(self, value: float)
```
Обновляет прогресс-бар.

#### start_scan()
```python
def start_scan(self)
```
Запускает сканирование.

#### run()
```python
def run(self)
```
Запускает приложение. 