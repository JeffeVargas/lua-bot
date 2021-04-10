import requests
import json

def getClimaByCidade(cidadeDigitada,nomeContato):
    requisicao = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+str(cidadeDigitada)+'&appid=3545b82c3b372729b1356b66bbcd32e5&lang=pt&units=metric')

    jsonResults = json.loads(str(requisicao.text))

    print (jsonResults)

    try:
        paisResultado = str(jsonResults['sys']['country']).title()
        cidadeResultado = str(jsonResults['name']).title()
        temperaturaResultado = str(jsonResults['main']['temp'])
        descricaoResultado = str(jsonResults['weather'][0]['description']).title()

        if nomeContato == None:
            mensagem = '$BOT - {}-{} está com {}, com uma temperatura de {}°!'.format(cidadeResultado,paisResultado.upper(),descricaoResultado,temperaturaResultado)
        else:
            mensagem = '$BOT - {}, {}-{} está com {}, com uma temperatura de {}°!'.format(nomeContato,cidadeResultado,paisResultado.upper(),descricaoResultado,temperaturaResultado)
    except:
        mensagem = '*$BOT - Hmm, não consegui encontrar a cidade que você digitou, você usou acentos?*'

    return mensagem

print (getClimaByCidade(
    'pompeia',
    'Jorge'
))