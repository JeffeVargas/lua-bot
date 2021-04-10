import requests
import json
import pyttsx3 as p
from config import api_key

engine = p.init()
keywords = ['qual', 'é o', 'clima', 'em']


def talk(text):
    engine.say(text)
    engine.runAndWait()

def findcity(trat_voice):

    for i in keywords:
        trat_voice = trat_voice.replace(i, '')
        city = trat_voice.title()
        city = city.strip()

    with open('./json/city.list.json', encoding="utf8") as f:
        data = json.load(f)
    
    for ct in data[0:]:
        list_city = (ct['name'], ct['id'])
        if city in list_city:
            city_id = list_city[1]
            city_name = list_city[0]
            getClimaByCidade(city_id, city_name)
            break

def getClimaByCidade(city_id, city_name):
    requisicao = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id='+str(city_id)+'&appid=' + api_key )
    
    jsonResults = json.loads(str(requisicao.text))

    try:
        paisResultado = str(jsonResults['sys']['country']).title()
        cidadeResultado = str(jsonResults['name']).title()
        temperaturaResultado = str(jsonResults['main']['temp'])
        descricaoResultado = str(jsonResults['weather'][0]['description']).title()

        talk(f'O clima em {cidadeResultado} - {(paisResultado).upper()} é de {temperaturaResultado[0:2]} graus')

    except:
        talk('ERROR')
