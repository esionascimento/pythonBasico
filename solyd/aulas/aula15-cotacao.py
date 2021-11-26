import requests
import json

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

print(requisicao.text)

cotacao = json.loads(requisicao.text)

print('### Cotação ###\n')
print('Dolar-Real: ', cotacao['USDBRL']['ask'])
print('Euro-Real: ', cotacao['EURBRL']['ask'])
print('Bitcoin-Real: ', cotacao['BTCBRL']['ask'])
