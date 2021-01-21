from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p
from datetime import datetime

class whatsapp():

    def __init__(self, nome, mensagem, send_time):
        self.nome = nome
        self.mensagem = mensagem
        self.send_time = send_time
        print(self.nome, self.mensagem, self.send_time)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url="https://web.whatsapp.com")
        while True:
            self.tempo = datetime.now()
            self.current_time = self.tempo.strftime("%H:%M")
            if self.current_time in self.send_time:
                bar = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
                bar.click()
                bar.send_keys(self.nome, Keys.ENTER)

                msg_bar = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
                msg_bar.send_keys(self.mensagem, Keys.ENTER)

                question = input('''Deseja continuar?
                
                [ s ] Sair
                [ e ] Enviar novamente
                
                Sua resposta: ''')
                if question == 's':
                    break