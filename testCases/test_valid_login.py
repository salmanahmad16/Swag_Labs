import time
import pytest
from selenium import webdriver
from pageObjects.loginPage import ValidLogin


class Test_Case_001_ValidLogin:
    baseUrl = 'https://www.saucedemo.com/'
    username = "standard_user"
    password = "secret_sauce"

    def test_validLogin(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.v_login = ValidLogin(self.driver)
        self.v_login.enterUserName(self.username)
        self.v_login.enterPassword(self.password)
        self.v_login.clickLoginButton()
        act_title = self.driver.title
        exp_title = "Swag Labs"
        if act_title == exp_title:
            print("Test Passed")
        else:
            print("Test Failed")
        self.v_login.clickLogoutButton()
        self.driver.quit()
