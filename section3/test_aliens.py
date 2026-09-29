import math
import os
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Логин и пароль берутся из переменных окружения, чтобы не хранить их в репозитории
LOGIN = os.environ.get("STEPIK_LOGIN")
PASSWORD = os.environ.get("STEPIK_PASSWORD")

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]


def login(browser, wait):
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".navbar__auth_login"))).click()
    wait.until(EC.visibility_of_element_located((By.ID, "id_login_email"))).send_keys(LOGIN)
    browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
    browser.find_element(By.CSS_SELECTOR, ".sign-form__btn").click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog-inner")))


@pytest.mark.skipif(not (LOGIN and PASSWORD), reason="не заданы STEPIK_LOGIN и STEPIK_PASSWORD")
@pytest.mark.parametrize("link", links)
def test_feedback_is_correct(browser, link):
    browser.get(link)
    wait = WebDriverWait(browser, 20)
    login(browser, wait)

    # Ждём, пока загрузится сама задача
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea")))

    # Если задача уже решалась раньше, поле заблокировано: нажимаем "Решить снова"
    again_buttons = browser.find_elements(By.CSS_SELECTOR, ".again-btn")
    if again_buttons:
        again_buttons[0].click()

    textarea = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea")))
    textarea.clear()

    # Ответ устаревает, поэтому считаем его прямо перед отправкой
    answer = math.log(int(time.time()))
    textarea.send_keys(str(answer))

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(normalize-space(), 'Отправить')]")
    )).click()

    feedback = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
    ).text
    assert feedback == "Correct!", f"Ожидался фидбек 'Correct!', получен '{feedback}'"
