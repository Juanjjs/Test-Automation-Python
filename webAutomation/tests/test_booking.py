import pytest
from utils.webdriver_setup import setup_browser
from pages.HomePage import HomePage
import time

# Fixture para inicializar y cerrar el navegador
@pytest.fixture(scope="function")
def browser():
    driver = setup_browser()
    yield driver  # Proporciona el navegador a la prueba
    driver.quit()  # Cierra el navegador al final de la prueba

# Caso de prueba para verificar la búsqueda de billetes
def test_search_ticket(browser):
    homepage = HomePage(browser)
    
    # Navegar a la página
    browser.get('https://www.renfe.com/es/es')  # Cambia 'URL_DE_LA_PAGINA' por la URL real

    # Interactuar con la página
    homepage.enter_origin("VALENCIA JOAQUÍN SOROLLA")
    homepage.enter_destination("BARCELONA-SANTS")
    homepage.select_date()
    homepage.confirm_trip()
    homepage.scroll_to_top()
    
    # Realizar la búsqueda
    homepage.search_tickets()

    # Verificar que la acción ha tenido éxito (puedes añadir tus propios checks, por ejemplo)
    # Aquí simplemente esperamos unos segundos para la carga de resultados
    time.sleep(5)
    
    # Verificamos si la URL ha cambiado (como indicativo de una búsqueda exitosa)
    assert "search-results" in browser.current_url, "No se encontraron los resultados de la búsqueda"

