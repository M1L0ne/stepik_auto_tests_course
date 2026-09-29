from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим картинку-сундук и берём значение атрибута valuex
    treasure = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    # Вводим ответ
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # Отмечаем чекбокс "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    # Выбираем radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Время, чтобы скопировать число из alert
    time.sleep(30)
finally:
    if browser:
        browser.quit()