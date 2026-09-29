import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):
    def fill_registration_form(self, link):
        browser = webdriver.Chrome()
        try:
            browser.get(link)

            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
            browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("ivan@example.com")

            browser.find_element(By.CSS_SELECTOR, "button.btn").click()

            time.sleep(1)  # даём странице загрузиться

            return browser.find_element(By.TAG_NAME, "h1").text
        finally:
            browser.quit()

    def test_registration1(self):
        welcome_text = self.fill_registration_form("http://suninjuly.github.io/registration1.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Неожиданный текст после регистрации")

    def test_registration2(self):
        # На этой странице нет поля фамилии, поэтому тест упадёт с NoSuchElementException
        welcome_text = self.fill_registration_form("http://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Неожиданный текст после регистрации")


if __name__ == "__main__":
    unittest.main()
