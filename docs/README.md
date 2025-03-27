# Документация Anti Evil Portal Scanner

## Содержание

1. [Общее описание](general.md)
2. [Архитектура](architecture.md)
3. [Модули](modules/README.md)
   - [NetworkManager](modules/network.md)
   - [EvilPortalAttacker](modules/attacker.md)
   - [ScannerUI](modules/ui.md)
4. [Конфигурация](configuration.md)
5. [Безопасность](security.md)
6. [Разработка](development.md)

## Краткое описание

Anti Evil Portal Scanner - это инструмент для обнаружения и защиты от Evil Portal атак на WiFi сети. Программа сканирует доступные сети, определяет потенциальные Evil Portal и применяет защитные меры.

## Основные компоненты

- `NetworkManager` - управление WiFi подключениями
- `EvilPortalAttacker` - реализация методов атаки
- `ScannerUI` - пользовательский интерфейс
- `config.py` - конфигурация приложения 