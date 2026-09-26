from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем на кнопку, после чего появляется confirm
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 2. Переключаемся на confirm и принимаем его
    confirm = browser.switch_to.alert
    confirm.accept()

    # 3. На новой странице решаем капчу
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Время, чтобы скопировать число из alert
    time.sleep(30)
finally:
    if browser:
        browser.quit()