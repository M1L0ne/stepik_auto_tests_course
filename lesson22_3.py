from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"

# Создаём пустой .txt файл рядом со скриптом
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")
with open(file_path, "w") as f:
    pass

browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем текстовые поля
    browser.find_element(By.CSS_SELECTOR, "[name='firstname']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "[name='lastname']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "[name='email']").send_keys("ivan@example.com")

    # Загружаем файл: передаём путь в input[type=file]
    browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Время, чтобы скопировать число из alert
    time.sleep(30)
finally:
    if browser:
        browser.quit()