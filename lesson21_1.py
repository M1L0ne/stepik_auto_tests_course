from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем x
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    # 2. Вводим ответ
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # 3. Отмечаем чекбокс "I'm the robot"
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    # 4. Выбираем radiobutton "Robots rule!"
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # 5. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Число из alert нужно успеть скопировать
    time.sleep(30)
finally:
    if browser:
        browser.quit()