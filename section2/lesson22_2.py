from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Считываем x и считаем функцию
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)

    # Вводим ответ
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    # Прокручиваем страницу так, чтобы кнопка оказалась в области видимости
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)

    # Отмечаем чекбокс и радиокнопку
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    # Нажимаем Submit
    button.click()

    # Время, чтобы скопировать число из alert
    time.sleep(30)
finally:
    if browser:
        browser.quit()