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

def doll():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.google.com/search?q=dolar')
    dolar = driver.find_element_by_xpath('/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/span[1]').text
    talk(f'O preço do dólar atual é de {dolar} reais')
    driver.quit()
