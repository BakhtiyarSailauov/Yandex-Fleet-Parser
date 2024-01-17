import random

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from auth_data import yandex_password, yandex_login
import time

# Указал путь к ChromeDriver
service = Service(r'C:\Users\Pavilion\PycharmProjects\yandex_analiz\chromedriver-win64\chromedriver.exe')
# Инициализировал драйвера
driver = webdriver.Chrome(service=service)
driver.get("https://fleet.yandex.ru")
time.sleep(2)
driver.find_element(By.XPATH, "//*[contains(text(),'Сменить логин')]").click()

email_input = driver.find_element(By.ID, "passp-field-login")
email_input.clear()
email_input.send_keys(yandex_login)
email_input.send_keys(Keys.ENTER)
time.sleep(2)

password_input = driver.find_element(By.ID, "passp-field-passwd")
password_input.clear()
password_input.send_keys(yandex_password)
time.sleep(3)
password_input.send_keys(Keys.ENTER)
time.sleep(5)

driver.refresh()
time.sleep(5)

while True:
    try:
        wait = WebDriverWait(driver, 10)

        # В начале вашего цикла обработки страниц
        current_page_url = driver.current_url

        # Получаем все ссылки на водителей
        links = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div/div/div[1]/div/div[1]/div[2]/main/div/table/tbody/tr/td[4]/a")))

        # Сохраняем атрибут href каждой ссылки в список urls
        urls = [link.get_attribute('href') for link in links]

        # Добавляем текущую URL страницы в конец списка urls
        urls.append(current_page_url)

        for url in urls:
            driver.get(url)

            try:
                time.sleep(random.randrange(5, 8))
                limit_element = driver.find_element(By.XPATH,
                                                    '/html/body/div/div/div[1]/div/div[1]/div[2]/main/div/form/div[1]/div[3]/div/div/div[1]/span/div[2]/div/div[2]/span/span/input')
                limit = limit_element.get_attribute('value')
                if int(limit) < 500000:
                    wait = WebDriverWait(driver, 10)
                    input_field = driver.find_element(By.XPATH,
                                                      '/html/body/div/div/div[1]/div/div[1]/div[2]/main/div/form/div[1]/div[3]/div/div/div[1]/span/div[2]/div/div[2]/span/span/input')
                    new_value = "-50"

                    # Clear the existing value by sending Ctrl+A and then Backspace
                    input_field.send_keys(Keys.CONTROL + 'a')
                    input_field.send_keys(Keys.BACKSPACE)
                    # Set the new value
                    input_field.send_keys(new_value)

                    save_button = driver.find_element(By.XPATH,
                                                      '/html/body/div/div/div[1]/div/div[1]/div[2]/main/div/form/div[2]/button/span/span')
                    save_button.click()
                    print(f"Saved value {new_value} from {limit} for driver at {url}")
                else:
                    print("Тут больше 500000!")
                    continue
            except NoSuchElementException:
                print(f"Element not found in {url}")
                continue
            except TimeoutException:
                print(f"Timeout waiting for elements in {url}")
                continue

        # Переход на следующую страницу
        next_page_button = driver.find_element(By.CSS_SELECTOR,
                                               "li.rc-pagination-next > button.rc-pagination-item-link")
        if not next_page_button:
            break  # Если кнопки следующей страницы нет, выходим из цикла
        next_page_button.click()
    except NoSuchElementException:
        print("Next page button not found, exiting.")
        break

# Завершение работы
driver.quit()
