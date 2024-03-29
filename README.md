# Документация к скрипту автоматизации Yandex Fleet

## Обзор

Скрипт `Autho_BOT.py` автоматизирует процесс входа в систему fleet.yandex.ru и обновления лимитов для водителей. Он предназначен для работы с веб-интерфейсом Yandex Fleet и позволяет автоматически изменять значения лимитов для водителей, чьи текущие лимиты ниже установленного порога.

## Настройка

Перед запуском убедитесь, что у вас установлены следующие зависимости:
- Python 3.6+
- Selenium WebDriver
- ChromeDriver (должен соответствовать версии вашего браузера Chrome)

Установите необходимые библиотеки с помощью команды:

pip install selenium


## Использование

Для запуска скрипта введите в терминале:

python Autho_BOT.py


## Описание работы скрипта

1. **Инициализация драйвера и вход в систему:**
   Скрипт начинается с инициализации WebDriver и открытия страницы входа fleet.yandex.ru. Затем осуществляется вход в систему с использованием предоставленных учетных данных.

2. **Перебор водителей и обновление лимитов:**
   После успешного входа в систему скрипт перебирает список водителей на текущей странице и проверяет значение их лимитов. Если лимит водителя ниже 500000, скрипт обновляет его до "-50".

3. **Переход на следующую страницу:**
   По завершении обновления лимитов на текущей странице, скрипт пытается найти и нажать кнопку для перехода на следующую страницу пагинации.

4. **Завершение работы:**
   Если кнопка следующей страницы не найдена, скрипт завершит работу и закроет браузер.

## Ошибки и их устранение

- Если скрипт не может найти элемент на странице, он выведет сообщение "Element not found" и продолжит обработку следующего элемента.
- В случае, если кнопка следующей страницы не найдена, скрипт выведет "Next page button not found, exiting." и завершит работу.


