from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class PaymentPage(BasePage):
    name_input_locator = (By.ID, "nombre0")
    lastname_input_locator = (By.ID, "apellido10")
    email_input_locator = (By.ID, "email0")
    phone_input_locator = (By.ID, "telefono0")

    def fill_personal_details(self, name, lastname, email, phone):
        self.send_keys(self.name_input_locator, name)
        self.send_keys(self.lastname_input_locator, lastname)
        self.send_keys(self.email_input_locator, email)
        self.send_keys(self.phone_input_locator, phone)
