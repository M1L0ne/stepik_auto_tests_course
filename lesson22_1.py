from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
# Проверьте также на: https://suninjuly.github.io/selects2.html

browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем числа и считаем сумму
    num1 = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    num2 = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    total = num1 + num2

    # 2. Выбираем в списке пункт, равный сумме
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(total))  # именно строка, не int

    # 3. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Время, чтобы скопировать число из alert
    time.sleep(30)
finally:
    if browser:
        browser.quit()