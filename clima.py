from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p

engine = p.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

class weather():

    def __init__(self, city):
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.name = city
        self.driver.get('https://www.google.com')
        bar = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input'))
        )
        bar.click()
        bar.send_keys(city, Keys.ENTER)

        temperature = self.driver.find_element_by_id('wob_tm').text
        rain = self.driver.find_element_by_id('wob_pp').text
        humity = self.driver.find_element_by_id('wob_hm').text
        wind = self.driver.find_element_by_id('wob_ws').text

        talk('A temperatura é de {} graus, precipitação de chuva de {}, umidade de {} e ventos à {}'.format(temperature, rain, humity, wind))

        self.driver.quit()
