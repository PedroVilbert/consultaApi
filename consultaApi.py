from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Iniciar o navegador Chrome
navegador = webdriver.Chrome()
# Acessar a página de horóscopos do site astro.com
navegador.get("https://www.astro.com/horoscope")
# Maximizar a janela do navegador para melhor visualização
navegador.maximize_window()

# Definir uma espera explícita de até 10 segundos para encontrar elementos na página
wait = WebDriverWait(navegador, 10)

# Esperar o botão do menu ficar clicável e clicar nele
menu_botao = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "img.navlink.navbar-toggler-left"))
)
menu_botao.click()

# Esperar o botão "Free Horoscopes" ficar clicável e clicar nele
bnt_free_horoscopes = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".rubrik.rubrik_0"))
)
bnt_free_horoscopes.click()

# Alternativa comentada: procurar todos os botões e clicar no que tem o texto "Free Horoscopes"
# lista_botoes_menu = navegador.find_elements(By.CSS_SELECTOR, "rubrik.rubrik_0")
# for botao in lista_botoes_menu:
#     if "Free Horoscopes"== botao.text:
#         botao.click()

# Esperar o botão "Horoscope Drawings & Data" ficar clicável e clicar nele
bnt_drawings_data = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Horoscope Drawings & Data']"))
)
bnt_drawings_data.click()

# Esperar o botão "Extended Chart Selection" ficar clicável e clicar nele
bnt_chart_selection = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[text()='Extended Chart Selection']"))
)
bnt_chart_selection.click()

# Esperar 10 segundos para visualizar o resultado antes de fechar o navegador
time.sleep(10)
# Fechar o navegador