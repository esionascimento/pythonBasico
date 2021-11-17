try:
  a = 1200 / 0
except ZeroDivisionError: #erro expecifico
  print("Divisao por zero, invalido")
except NameError:
  print("Você digitou alguma coisa errado")
except Exception as erro: #salva o erro na variavel para usar posteriormente
  print("Qualquer exceção", erro)

print("Hello")
