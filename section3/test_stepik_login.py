import os

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://stepik.org/lesson/236895/step/1"

# Логин и пароль берутся из переменных окружения, чтобы не хранить их в репозитории
LOGIN = os.environ.get("STEPIK_LOGIN")
PASSWORD = os.environ.get("STEPIK_PASSWORD")


@pytest.mark.skipif(not (LOGIN and PASSWORD), reason="не заданы STEPIK_LOGIN и STEPIK_PASSWORD")
def test_user_can_login(browser):
    browser.get(link)
    wait = WebDriverWait(browser, 15)

    # Stepik отрисовывает страницу через JavaScript, поэтому ждём появления кнопки "Войти"
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))).click()

    wait.until(EC.visibility_of_element_located((By.ID, "id_login_email"))).send_keys(LOGIN)
    browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()

    # Авторизация прошла, когда окно входа исчезло
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog-inner")))
