print('Hello World!\n')
print('segundo print')

nome = input('Escreva seu nome: ')
idade = input('Escreva sua idade: ')
altura = input('Escreva sua altura: ')
tipo_idade = type(idade)
tipo_altura = type(altura)

print(nome)
print(type(nome))
print(tipo_idade)
print(tipo_altura)
frase = nome, 'tem', idade, 'anos e', altura, 'de altura'
print(nome + ' tem ' + str(idade) + ' anos e ' + str(altura) + ' de altura')
print(frase)
