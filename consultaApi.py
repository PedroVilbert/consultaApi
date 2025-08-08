from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Iniciar navegador
navegador = webdriver.Chrome()
navegador.get("https://www.astro.com/horoscope")
navegador.maximize_window()

wait = WebDriverWait(navegador, 10)

# Esperar e clicar no botão do menu
menu_botao = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "img.navlink.navbar-toggler-left"))
)
menu_botao.click()

bnt_free_horoscopes = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".xrubrik.rubrik_0"))
)
bnt_free_horoscopes.click()
# lista_botoes_menu = navegador.find_elements(By.CSS_SELECTOR, "rubrik.rubrik_0")
# for botao in lista_botoes_menu:
#     if "Free Horoscopes"== botao.text:
#         botao.click()

lista2_botoes_menu = navegador.find_elements("class name", "inner show")


time.sleep(10)
navegador.quit()

