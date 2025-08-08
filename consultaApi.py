from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Abrir o navegador
navegador = webdriver.Chrome()

# Acessar o site
navegador.get("https://www.astro.com/horoscope")
navegador.maximize_window()

# Esperar a página carregar
time.sleep(3)

# Selecionar todos os links de signos (dentro da div com classe 'hpzod')
lista_botoes = navegador.find_elements(By.CSS_SELECTOR, ".hpzod a")

# Iterar pelos botões até encontrar o signo
signo = "Aries"
for botao in lista_botoes:
    texto = botao.get_attribute("innerHTML")
    if signo in texto:
        botao.click()
        break

# Esperar o conteúdo da nova página carregar
time.sleep(5)

# Extrair todos os parágrafos visíveis e juntar o texto
paragrafos = navegador.find_elements(By.TAG_NAME, "p")
texto_completo = "\n".join([p.text for p in paragrafos if p.text.strip() != ""])

# Limpar o texto removendo informações extras a partir de "Short excerpt"
indice = texto_completo.find("Short excerpt")
if indice != -1:
    texto_limpo = texto_completo[:indice].strip()
else:
    texto_limpo = texto_completo

print("Descrição limpa:\n")
print(texto_limpo)

# Esperar para leitura (opcional)
time.sleep(5)

# Fechar o navegador
navegador.quit()
