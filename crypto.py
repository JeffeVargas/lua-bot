import requests
from bs4 import BeautifulSoup
import pyttsx3 as p

engine = p.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def bat():
    r = requests.get('https://coinmarketcap.com/pt-br/currencies/basic-attention-token/')
    soup = BeautifulSoup(r.content, 'html.parser')
    price = soup.findAll(class_="priceValue___11gHJ")
    value = price[0].get_text()
    value = value.replace('R$', '')
    talk(value + 'reais')