import time
from pageObjects.basePage import BaseMethods
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class AddToCart(BaseMethods):
    button_addtocart_prod1 = (By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-backpack"]')
    button_addtocart_prod2 = (By.CSS_SELECTOR, 'button[id="add-to-cart-sauce-labs-bike-light"]')
    button_shoping_cart = (By.CSS_SELECTOR, 'div[id="shopping_cart_container"]>a')
    text_prod1_name = (By.CSS_SELECTOR, 'a[id="item_4_title_link"]>div')
    text_prod1_price = (By.CSS_SELECTOR, 'div:nth-child(3) > div.cart_item_label > div.item_pricebar > div')
    text_prod2_name = (By.CSS_SELECTOR, 'a[id="item_0_title_link"]>div')
    text_prod2_price = (By.CSS_SELECTOR, 'div:nth-child(4) > div.cart_item_label > div.item_pricebar > div')
    button_checkout = (By.ID, 'checkout')
    text_input_first_name = (By.ID, 'first-name')
    text_input_last_name = (By.ID, 'last-name')
    text_input_postal_code = (By.ID, 'postal-code')
    button_continue = (By.ID, 'continue')
    button_finish = (By.ID, 'finish')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base = BaseMethods(self.driver)

    def addToCartProd1(self):
        self.base.click(self.button_addtocart_prod1)

    def addToCartProd2(self):
        self.base.click(self.button_addtocart_prod2)

    def goToCart(self):
        self.base.click(self.button_shoping_cart)

    def getAddedItemNames(self):
        prod1_name = self.base.get_text(self.text_prod1_name)
        prod2_name = self.base.get_text(self.text_prod2_name)
        return prod1_name, prod2_name

    def getAddedItemsPrices(self):
        prod1_price = self.base.get_text(self.text_prod1_price)
        prod2_price = self.base.get_text(self.text_prod2_price)
        return prod1_price, prod2_price

    def clickOnCheckoutButton(self):
        self.base.click(self.button_checkout)

    def enterPersonalInfo(self, firstname, lastname, postalcode):
        self.base.send_values(self.text_input_first_name, firstname)
        self.base.send_values(self.text_input_last_name, lastname)
        self.base.send_values(self.text_input_postal_code, postalcode)

    def clickOnContinueButton(self):
        self.base.click(self.button_continue)

    def clickOnFinishButton(self):
        self.base.click(self.button_finish)
