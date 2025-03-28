# Устранение неполадок

## Общие проблемы

### Программа не запускается

1. Проверьте версию Python:
```bash
python --version
```
Должна быть 3.7 или выше.

2. Проверьте установку зависимостей:
```bash
pip list
```
Убедитесь, что все пакеты из requirements.txt установлены.

3. Проверьте права доступа:
- Windows: Запустите от имени администратора
- Linux: Добавьте пользователя в группу netdev
- macOS: Предоставьте доступ к WiFi

### Не работает сканирование

1. Проверьте WiFi адаптер:
- Включен ли WiFi
- Поддерживает ли мониторинг
- Не блокируется ли антивирусом

2. Проверьте настройки в .env:
- Правильные ли значения параметров
- Не слишком ли маленькие таймауты
- Достаточно ли потоков

3. Проверьте логи:
```bash
tail -f scanner.log
```

### Ошибки атаки

1. Проверьте подключение:
- Доступна ли сеть
- Правильный ли URL
- Не блокирует ли файрвол

2. Проверьте payload:
- Не слишком ли большой размер
- Правильный ли формат
- Не блокируется ли сервером

3. Проверьте таймауты:
- Увеличьте CONNECTION_TIMEOUT
- Уменьшите MAX_RETRIES
- Настройте SCAN_INTERVAL

## Специфичные проблемы

### Windows

1. Ошибка доступа к WiFi:
- Запустите от имени администратора
- Проверьте службу WLAN AutoConfig
- Обновите драйверы WiFi

2. Проблемы с pywifi:
- Установите последнюю версию
- Проверьте совместимость с адаптером
- Попробуйте другой WiFi адаптер

### Linux

1. Ошибка доступа к WiFi:
```bash
sudo usermod -a -G netdev $USER
```
Перезагрузите систему.

2. Проблемы с правами:
```bash
sudo chmod +x AntiEvilPortal.py
```

### macOS

1. Ошибка доступа к WiFi:
- Откройте Системные настройки
- Перейдите в Безопасность и конфиденциальность
- Предоставьте доступ программе

2. Проблемы с pywifi:
- Установите через pip3
- Проверьте версию Python
- Обновите систему 