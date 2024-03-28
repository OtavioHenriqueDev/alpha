from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
def abrir_chromium_headless():
    opcoes = Options()
    opcoes.add_argument("--headless")
    opcoes.add_argument("--private")
    opcoes.add_argument ('--disable-blink-features=AutomationControlled')
    #opcoes.add_experimental_option("detach", True)
    
    driver = webdriver.Chrome(options=opcoes)
    driver.get("https://www.bet365.com")
    time.sleep(5)
    btnLogin = driver.find_element(By.CSS_SELECTOR,".hm-MainHeaderRHSLoggedOutWide_Login")
    btnLogin.click()
    time.sleep(5)
    inputUser = driver.find_element(By.CSS_SELECTOR,".lms-StandardLogin_Username")
    inputUser.send_keys("otavio8bit")
    time.sleep(5)
    inputPass = driver.find_element(By.CSS_SELECTOR,".lms-StandardLogin_Password")
    inputPass.send_keys("!@#Skateboard123")
    time.sleep(5)
    btnEnter = driver.find_element(By.CSS_SELECTOR,".lms-LoginButton_Text")
    btnEnter.click()
    print("Hello World, Vc vai ser rico")



abrir_chromium_headless()