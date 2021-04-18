from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pyttsx3 as p
from config import crypto_api_key

engine = p.init()

def talk(text):
	engine.say(text),
	engine.runAndWait()

def tratament(trated_coin):
	trated_coin = trated_coin.lower()
	keywords = {'qual é o', 'preço do'}
	for i in keywords:
		if i in keywords:
			trated_coin = trated_coin.replace(i, '')
			trated_coin = trated_coin.strip()
			trated_coin = trated_coin.title()
			findPriceCoin(trated_coin)

def findPriceCoin(trated_coin):
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
	parameters = {
	'start':'1',
	'limit':'5000',
	'convert':'BRL'
	}
	headers = {
	'Accepts': 'application/json',
	'X-CMC_PRO_API_KEY': crypto_api_key,
	}

	session = Session()
	session.headers.update(headers)

	try:
		response = session.get(url, params=parameters)
		data = json.loads(response.text)
		with open('./json/currencies.json', 'w') as write_file:
			json.dump(data, write_file)
		
		with open('./json/currencies.json') as file:
			json_info = json.load(file)
			json_data = json_info["data"]
			for verify in json_data:
				if verify in json_data:
					name_coin = (verify["name"])
					price_coin = (verify["quote"])
					if name_coin == trated_coin:
						price_coin = str(price_coin).strip()
						real_price = price_coin[18:27]
						real_price = float(real_price)
						talk(f'O preço do {trated_coin} é de {real_price:.2f} reais')
						print(f'O preço do {trated_coin} é de {real_price:.2f} reais')

	except (ConnectionError, Timeout, TooManyRedirects) as e:
		print(e)
