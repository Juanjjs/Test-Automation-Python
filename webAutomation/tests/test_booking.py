import pytest
from utils.webdriver_setup import setup_browser
from pages.HomePage import HomePage

@pytest.fixture
def driver():
    driver = setup_browser()
    yield driver
    #driver.quit()

def test_search_ticket(driver):
    driver.get("https://www.renfe.com/es/es")
    home_page = HomePage(driver)
    
    home_page.close_cookies()
    home_page.set_origin("VALENCIA JOAQUÍN SOROLLA")
    home_page.set_destination("BARCELONA-SANTS")
    home_page.select_date("10")
    home_page.search_tickets()
