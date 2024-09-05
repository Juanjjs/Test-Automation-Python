from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class HomePage(BasePage):
    origin_input_locator = (By.ID, "origin")
    destination_input_locator = (By.ID, "destination")
    search_button_locator = (By.XPATH, "//span[contains(text(),'Buscar billete')]")
    cookie_button_locator = (By.ID, "onetrust-accept-btn-handler")

    def enter_origin(self, origin):
        self.send_keys(self.origin_input_locator, origin)

    def enter_destination(self, destination):
        self.send_keys(self.destination_input_locator, destination)

    def accept_cookies(self):
        try:
            self.click(self.cookie_button_locator)
        except Exception:
            print("No cookies found.")

    def click_search_button(self):
        self.scroll_into_view(self.search_button_locator)
        self.click(self.search_button_locator)
