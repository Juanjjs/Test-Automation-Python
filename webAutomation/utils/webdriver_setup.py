from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def setup_browser():
    options = Options()

    # Disable notifications
    prefs = {
        "profile.default_content_setting_values.notifications": 2  # 1: Allow, 2: Block
    }
    options.add_experimental_option("prefs", prefs)

    # Disable engine
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-search-engine-choice-screen")

    #Manage webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver
