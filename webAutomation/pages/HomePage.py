from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    origin_input_locator = (By.ID, "origin")
    destination_input_locator = (By.ID, "destination")
    origin_list_item_locator = (By.CSS_SELECTOR, "li#awesomplete_list_1_item_0")
    destination_list_item_locator = (By.CSS_SELECTOR, "li#awesomplete_list_2_item_0")
    date_input_locator = (By.ID, "first-input")
    trip_option_locator = (By.XPATH, "//span[@class='lightpick__border']")
    day_locator = (By.XPATH, "//div[contains(@class, 'lightpick__day') and text()='10']")
    agree_button_locator = (By.CLASS_NAME, "lightpick__apply-action-sub")
    search_button_locator = (By.XPATH, "//span[contains(text(),'Buscar billete')]")
    body_locator = (By.TAG_NAME, "body")
    
    # Actions
    def enter_origin(self, origin_text):
        origin_input = self.wait.until(EC.presence_of_element_located(self.origin_input_locator))
        origin_input.send_keys(origin_text)
        time.sleep(2)
        origin_list_item = self.wait.until(EC.visibility_of_element_located(self.origin_list_item_locator))
        origin_list_item.click()

    def enter_destination(self, destination_text):
        destination_input = self.wait.until(EC.presence_of_element_located(self.destination_input_locator))
        destination_input.send_keys(destination_text)
        time.sleep(2)
        destination_list_item = self.wait.until(EC.visibility_of_element_located(self.destination_list_item_locator))
        destination_list_item.click()
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            cookie_button.click()
            print("Closed cookies.")
        except:
            print("No cookies found.")

    def select_date(self):
        date_input = self.wait.until(EC.presence_of_element_located(self.date_input_locator))
        date_input.click()
        time.sleep(1)
        try:
            trip_option = self.wait.until(EC.element_to_be_clickable(self.trip_option_locator))
            self.driver.execute_script("arguments[0].click();", trip_option)
            print("One trip selected.")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(2)
        day = self.wait.until(EC.element_to_be_clickable(self.day_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", day)
        day.click()
        time.sleep(2)

    def confirm_trip(self):
        action_agree = ActionChains(self.driver)
        agree_button = self.wait.until(EC.element_to_be_clickable(self.agree_button_locator))
        action_agree.move_to_element(agree_button).click().perform()
        print("Agree button clicked.")

    def scroll_to_top(self):
        body = self.driver.find_element(*self.body_locator)
        body.send_keys(Keys.HOME)

    def search_tickets(self):
        search_button = self.wait.until(EC.visibility_of_element_located(self.search_button_locator))
        print("Click on 'Buscar billetes' button.")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_button).click().perform()
        print("Clicked 'Buscar billete' button.")

