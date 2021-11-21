import requests
import json # trabalha com json, tranforma json em objetos

req = None
site = 'https://www.omdbapi.com/?apikey=baf71168&t=interstellar'

try:
  req = requests.get(site)
except:
  print('Erro na conexão')
  exit()

dicionario = json.loads(req.text) # converte json em dicionario

print(dicionario, '\n')
print('Título:', dicionario['Title'])
print('Ano:', dicionario['Year'])
print('Diretor:', dicionario['Director'])
print('Atores:', dicionario['Actors'])
print('Nota:', dicionario['imdbRating'])