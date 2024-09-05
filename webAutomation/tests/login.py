from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

# Disable notifications
prefs = {
    "profile.default_content_setting_values.notifications": 2  # 1: Allow, 2: Block
}
options.add_experimental_option("prefs", prefs)

# Other existing options
options.add_experimental_option("detach", True)
options.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.renfe.com/es/es")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
origin_input = wait.until(EC.presence_of_element_located((By.ID, "origin")))
origin_input.send_keys("VALENCIA JOAQUÍN SOROLLA")
time.sleep(2)

list_item_1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li#awesomplete_list_1_item_0")))
list_item_1.click()

end_input = wait.until(EC.presence_of_element_located((By.ID, "destination")))
end_input.send_keys("BARCELONA-SANTS")
time.sleep(2)

#origin_input.send_keys(Keys.DOWN)
#origin_input.send_keys(Keys.RETURN)

list_item_2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li#awesomplete_list_2_item_0")))
list_item_2.click()

try:
    cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    cookie_button.click()
    print("Closed cookies.")
except:
    print("No cookies found.")

time.sleep(2)

date_input = wait.until(EC.presence_of_element_located((By.ID, "first-input")))
date_input.click()

time.sleep(1)

try:
    trip_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='lightpick__border']")))
    driver.execute_script("arguments[0].click();", trip_option)
    print("One trip selected.")
except Exception as e:
    print(f"Error: {e}")

time.sleep(2)

day = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'lightpick__day') and text()='10']")))
driver.execute_script("arguments[0].scrollIntoView(true);", day)
day.click()

time.sleep(2)

# ActionChains to button
action_agree = ActionChains(driver)
agree_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "lightpick__apply-action-sub")))
action_agree.move_to_element(agree_button).click().perform()
print("Agree button")

# Top page
body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.HOME)

# Looking for tickets
# Wait for the search button to be visible and ready for interaction
search_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Buscar billete')]")))
print("Click on a button Buscar billetes")

# Scroll to the button
driver.execute_script("arguments[0].scrollIntoView(true);", search_button)

# Use ActionChains to move to the element and click
actions = ActionChains(driver)
actions.move_to_element(search_button).click().perform()

print("Clicked 'Buscar billete' button with ActionChains")


#Pagina 2
# Step 1: Locate the div containing the train option (the entire row with ID 'tren_i_1')
train_row_element = wait.until(EC.visibility_of_element_located((By.ID, "tren_i_1"))
)

# Step 3: Click on the train row element (entire area)
actions = ActionChains(driver)
actions.move_to_element(train_row_element).click().perform()

# Step 2: Scroll to the train row element to ensure it's visible
driver.execute_script("arguments[0].scrollIntoView(true);", train_row_element)

print("Clicked on the train row corresponding to 'Precio más bajo'.")


# Step 1: Locate the fare option container (the div with class 'card-body')
fare_option_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'card-body')]//ul[@class='lista-opciones list-group list-group-flush']//li[1]"))
)

# Step 2: Scroll to the fare option element to ensure it's visible
#driver.execute_script("arguments[0].scrollIntoView(true);", fare_option_element)

# Step 3: Click the fare option (first element within 'li')
actions_price = ActionChains(driver)
actions_price.move_to_element(fare_option_element).click().perform()

print("Clicked the selected fare option.")
time.sleep(2)
# Localiza el botón "Seleccionar" usando el ID
boton_seleccionar = driver.find_element(By.ID, "btnSeleccionar")
boton_seleccionar.click()

# Localiza el botón "Seleccionar" usando el ID
boton_condiciones = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id='aceptarConfirmacionFareUpgrade']")))
print("Boton No, quiero continuar encontrado!")
actions_dont = ActionChains(driver)
actions_dont.move_to_element(boton_condiciones).click().perform()


#Pagina 3
name_input = wait.until(EC.presence_of_element_located((By.ID, "nombre0")))
name_input.send_keys("Amaris")

lastname_input = wait.until(EC.presence_of_element_located((By.ID, "apellido10")))
lastname_input.send_keys("Consulting")

surname_input = wait.until(EC.presence_of_element_located((By.ID, "apellido20")))
surname_input.send_keys("Company")

identify_input = wait.until(EC.presence_of_element_located((By.ID, "documento0")))
identify_input.send_keys("12345678Z")

email_input = wait.until(EC.presence_of_element_located((By.ID, "email0")))
email_input.send_keys("amaris@consulting.com")

phone_input = wait.until(EC.presence_of_element_located((By.ID, "telefono0")))
phone_input.send_keys("637123456")



# Localiza el botón "Personalizar" usando el ID
boton_personalizar = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submitpersonaliza']")))
print("Boton personalizado encontrado!")
driver.execute_script("arguments[0].scrollIntoView(true);", boton_personalizar)
actions_continue = ActionChains(driver)
actions_continue.move_to_element(boton_personalizar).click().perform()


# Localiza el botón "Personalizar-2" usando el ID
driver.execute_script("window.scrollBy(0, 100);")
boton_personalizar_two = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submitFormaPago']")))
print("Boton personalizado 2 encontrado!")
actions_continue_two = ActionChains(driver)
actions_continue_two.move_to_element(boton_personalizar_two).click().perform()

#Pagina 4
email_input_2 = wait.until(EC.presence_of_element_located((By.ID, "inputEmail")))
email_input_2.send_keys("amaris@consulting.com")

phone_input_2 = wait.until(EC.presence_of_element_located((By.ID, "telefonoComprador")))
phone_input_2.send_keys("637123456")

# ActionChains to button
radio_button = wait.until(EC.element_to_be_clickable((By.ID, "datosPago_cdgoFormaPago_tarjetaRedSys")))

# Usa ActionChains para desplazarte hasta el elemento y hacer clic
ActionChains(driver).move_to_element(radio_button).click().perform()

boton_nueva_tarjeta = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'target-puntos-renfe') and contains(@class, 'selecTarjeta')]")))
print("Boton nueva tarjeta encontrado!")
actions_card = ActionChains(driver)
actions_card.move_to_element(boton_nueva_tarjeta).click().perform()

time.sleep(2)
# Haz clic en el checkbox
checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='aceptarCondiciones']")))
actions_checkbox = ActionChains(driver)
actions_checkbox.move_to_element(checkbox).click().perform()
print("Checkbox clicado!")

# Localiza el botón "Seleccionar" usando el ID
driver.execute_script("window.scrollBy(0, 100);")
boton_pagar = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='butonPagar']")))
print("Boton de pago!")
#driver.execute_script("arguments[0].scrollIntoView();", boton_pagar)
actions_pay = ActionChains(driver)
actions_pay.move_to_element(boton_pagar).click().perform()

#Pagina 5
number_card_input = wait.until(EC.presence_of_element_located((By.ID, "inputCard")))
number_card_input.send_keys("000000000000")

month_card_input = wait.until(EC.presence_of_element_located((By.ID, "cad1")))
month_card_input.send_keys("03")

year_card_input = wait.until(EC.presence_of_element_located((By.ID, "cad2")))
year_card_input.send_keys("27")

code_card_input = wait.until(EC.presence_of_element_located((By.ID, "codseg")))
code_card_input.send_keys("123")

# Localiza el botón "Pagar" usando el ID
boton_pay_final = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='divImgAceptar']")))
print("Aceptar pago final!")
actions_pay_final = ActionChains(driver)
actions_pay_final.move_to_element(boton_pay_final).click().perform()

print("Tarjeta no valida, cerrar navegador!")
time.sleep(3)
driver.quit()
