from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
import os

class create_profile():

    def desktop_start(self):
            # Caminho para o executável do WebDriver
            path_to_webdriver = "msedgedriver.exe"

            Profile = f'Profiles/telegram'
            # Define as opções do Chrome
            self.ChromeOptions = Options()
            # Define o caminho para o diretório de perfil do usuário
            self.profile = os.path.join(os.getcwd(),Profile)
            self.ChromeOptions.add_argument(f"--user-data-dir={self.profile}")
            self.ChromeOptions.add_experimental_option("detach", True)
            self.ChromeOptions.add_argument('--disable-blink-features=AutomationControlled')
            self.ChromeOptions.add_argument('--disable-gpu')
            self.ChromeOptions.add_argument("--disable-features=HeavyAdPrivacyMitigations") # ads chrome
            self.ChromeOptions.add_argument("--no-first-run")
            self.ChromeOptions.add_argument("--no-default-browser-check")
            self.ChromeOptions.add_argument("--disable-default-apps")
            self.ChromeOptions.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
            
            # Cria uma nova instância do WebDriver com as opções definidas
            self.DesktopDriver = WebDriver(options=self.ChromeOptions)

            self.DesktopDriver.get('https://www.bet365.com')
            time.sleep(30)




            self.DesktopDriver.quit()



bot_login = create_profile()

bot_login.desktop_start()