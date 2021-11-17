import time

try:
  a = 1200 / 0
except ZeroDivisionError: #erro expecifico
  print("Divisao por zero, invalido")
except NameError:
  print("Você digitou alguma coisa errado")
except Exception as erro: #salva o erro na variavel para usar posteriormente
  print("Qualquer exceção", erro)

print("Hello")

def abre_arquivo():
  try:
    abre_arquivo = open('arquivo1.txt')
    return True
  except Exception as erro:
    print("Erro:", erro)
    return False

while not abre_arquivo():
  print("Tentando abrir o arquivo")
  time.sleep(5)

print("Consegui abrir o arquivo")