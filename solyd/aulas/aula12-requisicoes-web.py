""" Para sistemas UNIX*

sudo apt-get install python3-pip # para instalar o pip3
sudo rm /usr/bin/pip # caso você tenha o pip já instalado
sudo mv /usr/bin/pip3 /usr/bin/pip # apenas para renomear o arquivo e tornálo mais acessivél .....
sudo pip install --upgrade pip # atualizar para a última versão do gerenciador pip """
import requests

try:
  requisicao = requests.get('http://g1.com.br')
  print(requisicao)
  print(requisicao.status_code)
  print(requisicao.text)
except Exception as e:
  print("Requisicao deu erro:", e)
