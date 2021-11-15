nomes = ['Guilherme', 'Marcelo', 'João', 'Júlia']

lista_de_numeros = range(5)#cria uma lista de números

for i in lista_de_numeros:
  print(i)#0,1,2,3,4

#para cada 'nome' dentro de 'nomes'
for nome in nomes:
  print(nome)

for item in range(0, 10, 2):
  print(item)

for item in range(len(nomes)):
  print(nomes[item])

palavra = 'Esio Rodrigues'

for letra in palavra:#imprime cada letra
  print(letra)