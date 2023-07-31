import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import InvalidLogin


class Test_Case_002_InvalidLogin:
    baseUrl = 'https://www.saucedemo.com/'
    username = "standard"
    password = "secret"
    error_text = 'Epic sadface: Username and password do not match any user in this service'

    def test_invalidLogin(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.inv_login = InvalidLogin(self.driver)
        self.inv_login.enterUserName(self.username)
        self.inv_login.enterPassword(self.password)
        self.inv_login.clickLoginButton()
        if self.inv_login.getErrorMessage() == self.error_text:
            print("Test Pass")
        else:
            print("Test Failed")


