import requests
import json # trabalha com json, tranforma json em objetos

site = 'https://www.omdbapi.com/?apikey=baf71168&t='

def requisicao(titulo):
  try:
    req = requests.get(site + titulo)
    dicionario = json.loads(req.text) # converte json em dicionario
    return dicionario
  except:
    print('Erro na conexão')
    return None

def printar_detalhes(film):
  print('===Filme===')
  print('Título:', film['Title'])
  print('Ano:', film['Year'])
  print('Diretor:', film['Director'])
  print('Atores:', film['Actors'])
  print('Nota:', film['imdbRating'])
  print('')

sair = False
while not sair:
  op = input('Escreva o nome de um filme ou SAIR para fechar: ')

  if op == 'SAIR':
    sair = True
  else:
    film = requisicao(op)
    if film['Response'] == 'False':
      print('Filme não encontrado')
    else:
      printar_detalhes(film)