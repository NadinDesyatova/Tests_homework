import unittest
import time

from parameterized import parameterized
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestYandexLogIn(unittest.TestCase):
    def setUp(self):
        self.browser = Chrome()
        self.browser.get("https://passport.yandex.ru/auth/")

    def test_login_success(self):
        login = WebDriverWait(self.browser, 1).until(
            expected_conditions.presence_of_element_located((By.ID, "passp-field-login"))
        )
        login.send_keys("your_login")
        login.send_keys(Keys.RETURN)

        # time.sleep(5)

        password = WebDriverWait(self.browser, 3).until(
            expected_conditions.presence_of_element_located((By.ID, "passp-field-passwd"))
        )
        password.send_keys("your_password")
        password.send_keys(Keys.RETURN)

        time.sleep(3)

        current_url = self.browser.current_url
        self.assertEqual(current_url, "https://id.yandex.ru/")

    @parameterized.expand([
        ["empty_login", "", "Логин не указан"],
        ["invalid_characters", "invalid_characters", "Такой логин не подойдет"],
        ["login_not_exist", "lhjhjklj", "Нет такого аккаунта. Проверьте логин или войдите по телефону"]
    ])
    def test_enter_incorrect_login(self, type_error, incorrect_login, error_massage):
        login = WebDriverWait(self.browser, 1).until(
            expected_conditions.presence_of_element_located((By.ID, "passp-field-login"))
        )
        login.send_keys(incorrect_login)
        login.send_keys(Keys.RETURN)

        time.sleep(3)

        message_about_error = WebDriverWait(self.browser, 1).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "Textinput-Hint"))
        )

        self.assertEqual(message_about_error.text, error_massage)

    @parameterized.expand([
        ["empty_password", "", "Пароль не указан"],
        ["invalid password", "lhjhjklj", "Неверный пароль"]
    ])
    def test_enter_incorrect_password(self, type_error, incorrect_password, error_massage):
        login = WebDriverWait(self.browser, 1).until(
            expected_conditions.presence_of_element_located((By.ID, "passp-field-login"))
        )
        login.send_keys("your_login")
        login.send_keys(Keys.RETURN)

        # time.sleep(3)

        password = WebDriverWait(self.browser, 3).until(
            expected_conditions.presence_of_element_located((By.ID, "passp-field-passwd"))
        )
        password.send_keys(incorrect_password)
        password.send_keys(Keys.RETURN)

        message_about_error = WebDriverWait(self.browser, 1).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "Textinput-Hint"))
        )

        self.assertEqual(message_about_error.text, error_massage)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored', '-v'], exit=False)