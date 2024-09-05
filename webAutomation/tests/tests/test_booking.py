import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.HomePage import HomePage
from pages.SelectionPage import SelectionPage
from pages.PaymentPage import PaymentPage
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def setup():
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.renfe.com/es/es")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_booking_flow(setup):
    driver = setup
    
    # Interacción con la página de inicio
    home_page = HomePage(driver)
    home_page.enter_origin("VALENCIA JOAQUÍN SOROLLA")
    home_page.enter_destination("BARCELONA-SANTS")
    home_page.accept_cookies()
    home_page.click_search_button()
    
    # Selección de tren
    train_selection_page = SelectionPage(driver)
    train_selection_page.select_train()
    train_selection_page.select_fare_option()

    # Información de pago
    payment_page = PaymentPage(driver)
    payment_page.fill_personal_details("Amaris", "Consulting", "amaris@consulting.com", "637123456")
