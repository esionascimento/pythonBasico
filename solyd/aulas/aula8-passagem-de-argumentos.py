import sys #comunicar com o sos

argumentos = sys.argv #arg1 metod // arg2 n1 //arg3 n2

def soma(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2


if argumentos[1] == "soma":
  resp = soma(float(argumentos[2]), float(argumentos[3]))

elif argumentos[1] == "sub":
  resp = sub(float(argumentos[2]), float(argumentos[3]))

print(resp)

# tratar caso 'python3 aula8-passagem-de-argumentos.py sub 300' for passado menos argumentos < 3