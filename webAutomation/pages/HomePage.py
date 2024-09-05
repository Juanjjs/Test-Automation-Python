from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def close_cookies(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            cookie_button.click()
            print("Closed cookies.")
        except:
            print("No cookies found.")

    def set_origin(self, origin):
        origin_input = self.wait.until(EC.presence_of_element_located((By.ID, "origin")))
        origin_input.send_keys(origin)
        time.sleep(2)
        list_item_1 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li#awesomplete_list_1_item_0")))
        list_item_1.click()

    def set_destination(self, destination):
        end_input = self.wait.until(EC.presence_of_element_located((By.ID, "destination")))
        end_input.send_keys(destination)
        time.sleep(2)
        list_item_2 = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li#awesomplete_list_2_item_0")))
        list_item_2.click()

    def select_date(self, day):
        date_input = self.wait.until(EC.presence_of_element_located((By.ID, "first-input")))
        date_input.click()
        time.sleep(1)

        trip_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='lightpick__border']")))
        self.driver.execute_script("arguments[0].click();", trip_option)
        print("One trip selected.")
        time.sleep(2)

        day_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'lightpick__day') and text()='{day}']")))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", day_element)
        day_element.click()
        time.sleep(2)

        agree_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lightpick__apply-action-sub")))
        ActionChains(self.driver).move_to_element(agree_button).click().perform()

    def search_tickets(self):
        # Top page 
        body = self.driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.HOME)

        search_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Buscar billete')]")))
        print("Click on a button Buscar billetes")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_button)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_button).click().perform()

        print("Clicked 'Buscar billete' button with ActionChains")