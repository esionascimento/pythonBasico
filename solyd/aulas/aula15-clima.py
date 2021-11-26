import requests
import json

cidade = input("Escreva sua cidade: ")

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+ cidade +'&appid=0424c16a2d977c5c88f52bc476c7a7b1')

print(requisicao.text)

tempo = json.loads(requisicao.text)

print('Condição do tempo:', tempo['weather'][0]['main'])
print('Temperatura:', float(tempo['main']['temp']) -273.15)