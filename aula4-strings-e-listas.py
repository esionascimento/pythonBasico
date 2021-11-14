frase = 'Oi, tudo bem?'
lista_nomes = ['Joao', 'Maria', 'Guilherme', 'Esio']
lista_nomes.append('Rodrigues')#insere no ultimo index da lista
lista_nomes.remove('Joao')#remove o Joao da lista
lista_nomes.insert(1, 'Nascimento')#adiciona nome na lista, na posição desejada
lista_nomes[0] = 'Silva'#mudar valor no index 0 da lista
contador_esio = lista_nomes.count('Esio')#quantas vezes repete Esio na lista

print(lista_nomes)
print(lista_nomes.pop())#remove o ultimo index
print(lista_nomes)

print(len(lista_nomes))#quantos intens a na lista
print(contador_esio)
print(type(lista_nomes))
print(lista_nomes[0])
print(lista_nomes[0:2])#não imprime até o index 1
print(lista_nomes[-1])#imprime o ultimo n, conta de trás para frente
print(lista_nomes[-1:-4:-1])#imprime ['Esio', 'Guilherme', 'Maria'] o index 4 não incluso


print(frase[0:10])
print(frase[0:13:2])#inicia-do-0-ate-o-13-pulando-2
print(frase[::-1])#imprime ?meb odut ,iO de trás para frente
print(frase.lower())#retorna uma lista tudo minuscula, mas não altera o valor da variavel
frase_separada = frase.split(',')#transforma em uma lista onde encontrar uma ','
print(frase_separada)

lista_nomes.clear()#limpa lista
