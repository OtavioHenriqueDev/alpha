from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def abrir_chromium_headless():
    opcoes = Options()
    opcoes.add_argument("--headless")

    driver = webdriver.Chrome(options=opcoes)
    driver.get("https://www.bet365.com")

    try:
        # Espera até 10 segundos até que o elemento esteja presente
        btnLogin = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".hm-MainHeaderRHSLoggedOutWide_Login"))
        )
    finally:
        driver.quit()

abrir_chromium_headless()