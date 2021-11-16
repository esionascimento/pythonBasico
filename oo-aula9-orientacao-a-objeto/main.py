from veiculo import Veiculo
from carro import Carro

veiculo1 = Veiculo('preto', 6, 'ford', 30)

print(veiculo1)
print(type(veiculo1))

print("Carro 1")
print("Cor:", veiculo1.cor)
print("Rodas:", veiculo1.rodas)
print("Marca:", veiculo1.marca)

print("")
veiculo2 = Carro('branco', 4, 'bmw', 50)

print("Carro 2")
print("Cor:", veiculo2.cor)
print("Rodas:", veiculo2.rodas)
print("Marca:", veiculo2.marca)
print("Tanque", veiculo2.tanque)
veiculo2.abastecer(35)
print("Tanque", veiculo2.tanque)