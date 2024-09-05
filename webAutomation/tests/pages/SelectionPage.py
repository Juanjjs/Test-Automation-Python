from selenium.webdriver.common.by import By
from pages.BasePage import BasePage

class SelectionPage(BasePage):
    train_row_locator = (By.ID, "tren_i_1")
    fare_option_locator = (By.XPATH, "//div[contains(@class, 'card-body')]//ul[@class='lista-opciones list-group list-group-flush']//li[1]")

    def select_train(self):
        self.scroll_into_view(self.train_row_locator)
        self.click(self.train_row_locator)

    def select_fare_option(self):
        self.click(self.fare_option_locator)
