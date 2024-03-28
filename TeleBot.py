from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os
import time
import json

class BotMain():
    def configBrowser(self):
        Profile = f'data/Profiles/telegram'
        # define as opções do Chrome
        self.EdgeOptions = Options()
        self.profile = os.path.join(os.getcwd(),Profile)
        self.EdgeOptions.add_argument(f"--user-data-dir={self.profile}")
        self.EdgeOptions.add_experimental_option("detach", True)
        self.EdgeOptions.add_argument ('--disable-blink-features=AutomationControlled')
        self.EdgeOptions.add_argument('--disable-gpu')
        self.EdgeOptions.add_argument("--disable-features=HeavyAdPrivacyMitigations") # ads chrome
        self.EdgeOptions.add_argument("--no-first-run")
        self.EdgeOptions.add_argument("--no-default-browser-check")
        self.EdgeOptions.add_argument("--disable-default-apps")
        self.EdgeOptions.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        self.EdgeOptions.add_argument("--no-sandbox")
        self.EdgeOptions.add_argument("--disable-dev-shm-usage")
        self.EdgeOptions.add_argument("--disable-gpu")
        self.EdgeOptions.add_argument("--remote-debugging-port=9222")
        # Cria uma nova instância do WebDriver com as opções definidas
        self.DesktopDriver = WebDriver(options=self.EdgeOptions)

    def startBot(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(5)
        print('Entrando no grupo do telegram')
        self.DesktopDriver.get('https://web.telegram.org/a/#-1002030205235')
        time.sleep(5)
        try:
            self.scroll = self.DesktopDriver.find_element(By.CSS_SELECTOR,'button.Button.cxwA6gDO.default.secondary.round[aria-label="Go to bottom"]')
            self.scroll.click()
        except:
            pass

    def seachMessage(self):
        while True:
            with open('data/config/data.json', 'r') as f:
                data = json.load(f)
            self.NewID = data['MonitorBot']['Tools']['NewID']
            try:
                self.receiveMessage = self.DesktopDriver.find_element(By.XPATH,f"//div[contains(@data-message-id,'{str(self.NewID)}')]")
                print(f'Mensagem encontrado com id: {self.NewID}')
                time.sleep(3)
                main.getInfo()
                time.sleep(3)
                try:
                    # Gravar NewID em LastID
                    data['MonitorBot']['Tools']['LastID'] = self.NewID
                    # Escrever as alterações de volta para o arquivo
                    with open('data/config/data.json', 'w') as f:
                        json.dump(data, f, indent=4)
                    time.sleep(3)
                    main.toolID()
                except Exception as e:
                    print(f"Erro em gravar no banco de dados {str(e)}")
            except:
                print("Verificando Novas mensagens em 10s")
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                print('Verificando Novas mensagens em 10s\n(1)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(2)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(3)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(4)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(5)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(6)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(7)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(8)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(9)'),time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Verificando Novas mensagens em 10s\n(10)')
                print('Sem novos palpites'),time.sleep(1)


    def toolID(self):
            with open ('data/config/data.json','r') as f:
                data = json.load(f)
        
            self.LastID = int(data['MonitorBot']['Tools']['LastID'])
            self.NewID = int(data['MonitorBot']['Tools']['NewID'])

            try:
                if self.NewID == self.LastID:
                    NewId = self.NewID + 1
                    data['MonitorBot']['Tools']['NewID'] = NewId
                    with open('data/config/data.json', 'w') as f:
                        json.dump(data, f, indent=4)
                else:
                    print('Erro02 em toolID')
            except:
                print('Erro01 em toolID')

    def getInfo(self):
        try:
            #pegando informaçoes das mensagem
            self.infoMessage = self.DesktopDriver.find_element(By.XPATH, f"//div[contains(@data-message-id, '{str(self.NewID)}')]//div[contains(@class,'text-content clearfix with-meta')]")
            self.textMessage = self.infoMessage.text
            self.lines = self.textMessage.split('\n')
            self.oneLine = self.lines[0]
            self.thirdLine = self.lines[3]
            print(self.oneLine)
            self.times = self.thirdLine.split()
            self.time1, self.time2, self.time3, self.time4 = self.times
            print(self.time1)
            print(self.time2)
            print(self.time3)
            print(self.time4)
            time.sleep(3)
            main.saveInfo()
        except:
            print('Vericando Novas Mensagens')
        
    def saveInfo(self):
        # Verifica se o arquivo existe
        if os.path.exists('data/infos/data.json'):
            with open('data/infos/data.json', 'r') as f:
                data = json.load(f)
        else:
        # Cria um novo dicionário se o arquivo não existir
            data = {'Message': {}}

        # Adiciona os novos dados
        if self.NewID not in data['Message']:
            data['Message'][self.NewID] = []

        data['Message'][self.NewID].append(
            {
                "Id": self.NewID,
                "league": self.oneLine,
                "Try01": self.time1,
                "Try02": self.time2,
                "Try03": self.time3
            }
        )

        # Escreve os dados de volta no arquivo
        with open('data/infos/data.json', 'w') as f:
            json.dump(data, f, indent=4)
    

    def exitBot(self):
        self.DesktopDriver.quit()

main = BotMain()
main.configBrowser()
main.startBot()
main.seachMessage()



