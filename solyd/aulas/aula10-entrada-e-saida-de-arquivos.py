arquivo = open('arquivo.txt', 'w')

type(print(arquivo))

arquivo.write("Eai\n")

for i in range(0, 1000):
  arquivo.write(str(i)+"\n")

arquivo = open('arquivo.txt', 'r')

print(arquivo.read())

for linha in arquivo:
  print(linha)