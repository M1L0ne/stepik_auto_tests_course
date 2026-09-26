from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем на кнопку, после чего открывается новая вкладка
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 2. Переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # 3. Решаем капчу
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Время, чтобы скопировать число из alert
    time.sleep(30)
finally:
    if browser:
        browser.quit()