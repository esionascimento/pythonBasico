from veiculo import Veiculo

class Carro(Veiculo):

  def __init__(self, cor, rodas, marca, tanque):
    Veiculo.__init__(self, cor, rodas, marca, tanque)

  def abastecer(self, litros):
    if self.tanque + litros > 50:
      print("erro: tanque capacidade inferior")
    else:
      self.tanque += litros