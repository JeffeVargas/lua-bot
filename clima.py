from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pyttsx3 as p

engine = p.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def weather(city):
    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    city = city.replace(' ', '+')
    driver.get('https://www.google.com/search?q=' + city)

    temperature = driver.find_element_by_id('wob_tm').text
    rain = driver.find_element_by_id('wob_pp').text
    humity = driver.find_element_by_id('wob_hm').text
    wind = driver.find_element_by_id('wob_ws').text
    talk('A temperatura é de {} graus, precipitação de chuva de {}, umidade igual {} e ventos {}'.format(temperature, rain, humity, wind))
    driver.quit()