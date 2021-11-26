import re

string_de_teste = 'O gato é bonito'

padrao = re.search(r'gat\w', string_de_teste)
#gat. '.' -> qualquer caracter
#search -> primeira incidencia
padrao1 = re.findall(r'gat\w+', string_de_teste)
#findall -> todas ocorrencias salvando numa lista
#gat\w+ '+' -> uma ou mais vezes
if padrao:
  print(padrao.group())
else :
  print("Padrao nao encontrado")

print(r"Oi pessoal\nsegunda linha") #o r no começo tira o poder dos caracteres especiais, não quebrando linha e sim imprimindo o \n

