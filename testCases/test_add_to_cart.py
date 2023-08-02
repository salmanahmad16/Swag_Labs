from pageObjects.addtocartPage import AddToCart
from selenium import webdriver
from pageObjects.loginPage import ValidLogin
from selenium.webdriver.chrome.options import Options


class Test_Case_003_AddToCart:
    baseUrl = 'https://www.saucedemo.com/'
    username = "standard_user"
    password = "secret_sauce"
    error_text = 'Epic sadface: Username and password do not match any user in this service'
    prod1_name = "Sauce Labs Backpack"
    prod2_name = "Sauce Labs Bike Light"
    prod1_price = "$29.99"
    prod2_price = "$9.99"

    def test_add_to_cart(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.login = ValidLogin(self.driver)
        self.cart = AddToCart(self.driver)
        self.login.enterUserName(self.username)
        self.login.enterPassword(self.password)
        self.login.clickLoginButton()
        self.cart.addToCartProd1()
        self.cart.addToCartProd2()
        self.cart.goToCart()
        prod_name1, prod_name2 = self.cart.getAddedItemNames()
        prod_price1 , prod_price2 = self.cart.getAddedItemsPrices()

        assert prod_name1 in self.prod1_name
        assert prod_price1 in self.prod1_price
        assert prod_name2 in self.prod2_name
        assert prod_price2 in self.prod2_price

        self.cart.goToCart()
        self.cart.clickOnCheckoutButton()
        self.cart.enterPersonalInfo("salman", "ahmad", "12344")
        self.cart.clickOnContinueButton()
        self.cart.clickOnFinishButton()





