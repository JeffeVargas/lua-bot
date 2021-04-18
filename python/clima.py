import requests
import json
import sys
import pyttsx3 as p
from config import api_key

engine = p.init()
keywords = ['qual', 'é o', 'clima', 'em']


def talk(text):
    engine.say(text)
    engine.runAndWait()

def findcity(trat_voice):

    for select_city in keywords:
        trat_voice = trat_voice.replace(select_city, '')
        city = trat_voice.title()
        city = city.strip()

    with open('./json/city.lsit.json', encoding="utf8") as f:
        data = json.load(f)
    
    for city_json in data[0:]:
        list_city = (city_json['name'], city_json['id'])
        if (city in list_city):
            city_id = list_city[1]
            city_name = list_city[0]
            getWeatherByCity(city_id, city_name)
            break

    if (city not in list_city):
        talk('Cidade não encontrada... Por favor, tente novamente.')
        print('Cidade não encontrada... Por favor, tente novamente.')

def getWeatherByCity(city_id, city_name):
    request = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id='+str(city_id)+'&appid=' + api_key )

    jsonResults = json.loads(str(request.text))

    try:
        Country = str(jsonResults['sys']['country']).title()
        City = str(jsonResults['name']).title()
        Temperature = str(jsonResults['main']['temp'])
        Winds = str(jsonResults['wind']['speed'])
        Winds = Winds[0:1]
        Temperature = Temperature[0:2]

        talk(f'O clima em {City} - {(Country).upper()} é de {Temperature[0:2]} graus e ventos a {Winds[0:1]} kilometros por hora')
        print(f'O clima em {City} - {(Country).upper()} é de {Temperature[0:2]} graus e ventos a {Winds[0:1]} kilometros por hora')
    except:
        talk('Informações não encontradas')
