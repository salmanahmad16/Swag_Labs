import time
from pageObjects.basePage import BaseMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class ValidLogin(BaseMethods):
    text_username = (By.ID, 'user-name')
    text_password = (By.ID, 'password')
    button_login = (By.ID, 'login-button')
    text_error_message = (By.CSS_SELECTOR, '.error-message-container>h3')
    button_side_menu = (By.CSS_SELECTOR, 'button[id="react-burger-menu-btn"]')
    button_logout = (By.CSS_SELECTOR, 'a[id="logout_sidebar_link"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def enterUserName(self, username):
        self.base.send_values(self.text_username, username)

    def enterPassword(self, password):
        self.base.send_values(self.text_password, password)

    def clickLoginButton(self):
        self.base.click(self.button_login)

    def clickLogoutButton(self):
        self.base.click(self.button_side_menu)
        self.base.click(self.button_logout)


class InvalidLogin(BaseMethods):
    text_username = (By.ID, 'user-name')
    text_password = (By.ID, 'password')
    button_login = (By.ID, 'login-button')
    text_error_message = (By.CSS_SELECTOR, '.error-message-container>h3')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def enterUserName(self, username):
        self.base.send_values(self.text_username, username)

    def enterPassword(self, password):
        self.base.send_values(self.text_password, password)

    def clickLoginButton(self):
        self.base.click(self.button_login)

    def getErrorMessage(self):
        text = self.base.get_text(self.text_error_message)
        return text

