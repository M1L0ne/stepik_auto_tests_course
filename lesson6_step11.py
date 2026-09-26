from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Для проверки на странице с багом замените ссылку на:
# http://suninjuly.github.io/registration2.html
link = "http://suninjuly.github.io/registration1.html"

browser = None
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Селекторы привязаны к первому блоку и к уникальному классу поля,
    # поэтому каждый находит ровно один элемент
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("ivan@example.com")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)  # даём странице загрузиться

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert welcome_text == "Congratulations! You have successfully registered!", \
        f"Неожиданный текст: {welcome_text}"
    print("Тест пройден:", welcome_text)
finally:
    time.sleep(5)  # чтобы успеть посмотреть результат
    if browser:
        browser.quit()