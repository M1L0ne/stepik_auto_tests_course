from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ждём (до 15 секунд), пока цена станет $100
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем "Book"
    browser.find_element(By.ID, "book").click()

    # 3. Решаем задачу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    browser.find_element(By.ID, "answer").send_keys(y)

    # 4. Отправляем решение
    browser.find_element(By.ID, "solve").click()

    # Время, чтобы скопировать число из alert
    time.sleep(30)
finally:
    if browser:
        browser.quit()