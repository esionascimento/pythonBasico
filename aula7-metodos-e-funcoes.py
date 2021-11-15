print('Olá mundo')
print(len('Ola mundo')) #'9'



def soma(numero1, numero2):
  resp = numero1 + numero2
  return resp

retorno = soma(75, 1289)
print(retorno)

def imprime_oi():
  print('OI')

imprime_oi()

def tem_sete_itens(objeto):
  if len(objeto) == 7:
    return True
  else:
    return False

if tem_sete_itens('Oi pessoal'): #'false'
  print('tem mesmo 7 itens')

#função geralmente quando se passa um valor e ele retorna um valor

#metodo geralmente quando você passa um valor e não precisa de um retorno de valor