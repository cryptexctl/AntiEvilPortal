# ScannerUI

## Описание

ScannerUI - это модуль, реализующий пользовательский интерфейс приложения. Он обеспечивает:
- Отображение логов
- Управление прогрессом
- Обработку пользовательского ввода
- Визуальное представление результатов

## Основные функции

### Инициализация
```python
def __init__(self):
    self.window = ctk.CTk()
    self.window.title(WINDOW_TITLE)
    self.window.geometry(WINDOW_SIZE)
    
    self.setup_logging()
    self.setup_ui()
```

### Настройка логирования
```python
def setup_logging(self):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    self.logger = logging.getLogger(__name__)
```

### Настройка UI
```python
def setup_ui(self):
    # Создаем фрейм для логов
    log_frame = ctk.CTkFrame(self.window)
    log_frame.pack(fill="both", expand=True, padx=10, pady=5)

    # Создаем текстовое поле для логов
    self.log_text = ctk.CTkTextbox(log_frame, state='disabled')
    self.log_text.pack(fill="both", expand=True, padx=5, pady=5)

    # Создаем фрейм для кнопок
    button_frame = ctk.CTkFrame(self.window)
    button_frame.pack(fill="x", padx=10, pady=5)

    # Создаем кнопки
    self.scan_button = ctk.CTkButton(
        button_frame,
        text="Сканировать",
        command=self.start_scan
    )
    self.scan_button.pack(side="left", padx=5)

    self.clear_button = ctk.CTkButton(
        button_frame,
        text="Очистить",
        command=self.clear_logs
    )
    self.clear_button.pack(side="left", padx=5)

    # Создаем прогресс-бар
    self.progress_bar = ctk.CTkProgressBar(self.window)
    self.progress_bar.pack(fill="x", padx=10, pady=5)
    self.progress_bar.set(0)
```

### Добавление логов
```python
def add_log(self, text: str):
    self.log_text.configure(state='normal')
    self.log_text.insert("end", text + "\n")
    self.log_text.see("end")
    self.log_text.configure(state='disabled')
    self.logger.info(text)
```

### Очистка логов
```python
def clear_logs(self):
    self.log_text.configure(state='normal')
    self.log_text.delete("0.0", "end")
    self.log_text.configure(state='disabled')
    self.logger.info("Логи очищены")
```

### Обновление прогресса
```python
def update_progress(self, value: float):
    self.progress_bar.set(value)
```

### Запуск сканирования
```python
def start_scan(self):
    self.scan_button.configure(state='disabled')
    self.clear_logs()
    self.update_progress(0)
```

### Запуск приложения
```python
def run(self):
    self.window.mainloop()
```

## Использование

```python
# Создание экземпляра
ui = ScannerUI()

# Добавление лога
ui.add_log('Начало сканирования...')

# Обновление прогресса
ui.update_progress(0.5)

# Очистка логов
ui.clear_logs()

# Запуск приложения
ui.run()
```

## Компоненты интерфейса

1. **Окно приложения**
   - Заголовок
   - Размер
   - Тема

2. **Текстовое поле логов**
   - Отображение сообщений
   - Автопрокрутка
   - Состояние disabled

3. **Кнопки**
   - Сканировать
   - Очистить
   - Состояния

4. **Прогресс-бар**
   - Отображение прогресса
   - Обновление значения
   - Визуальный стиль

## Обработка событий

1. **Кнопка Сканировать**
   - Отключение кнопки
   - Очистка логов
   - Сброс прогресса

2. **Кнопка Очистить**
   - Очистка текстового поля
   - Логирование действия

3. **Обновление прогресса**
   - Установка значения
   - Обновление отображения 