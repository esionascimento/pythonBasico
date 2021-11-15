minha_lista = ['Gui', 'Joao'] #LISTA (list)
minha_tupla = ('Gui', 'Joao') #TUPLA (tuple) não pode alterar o tamanho
meu_dicionario = {'nome': 'Esio', 'idade': 23} #DICIONARIO (dict)
meu_conjunto = {'Gui', 'Joao'} #CONJUNTO (set) não pode ter valores repetidos, não existe indice

#tupla
print(minha_tupla)
print(minha_tupla[1])

for nome in minha_tupla:
  print(nome)

# minha_tupla[0] = 'Joao' # não aceita substituir desta forma
minha_tupla = ('Joao', 'Fabricio') #substitui toda a tupla
print(minha_tupla)

if 'Fabricio' in minha_tupla:
  print('Fabricio está na colecao')

# dicionario
print(meu_dicionario)
print(meu_dicionario['nome']) #busca pela chave

if 'Guilherme' in meu_dicionario: #não busca desta forma
  print('Guilherme está no dicionario')

if 'Guilherme' in meu_dicionario.values(): #busca desta forma
  print('Guilherme esta no dicionario')

for valores in meu_dicionario.values(): #nao esta ordenado
  print(valores)

for valores in meu_dicionario.keys(): #somente as chaves
  print(valores)

meu_dicionario['idade'] = '40' #mudando valores no dicionario
print(meu_dicionario)

meu_dicionario['endereco'] = 'Av. Hor' #adicionando nova chave no dicionario
print(meu_dicionario)