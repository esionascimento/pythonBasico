""" Para sistemas UNIX*

sudo apt-get install python3-pip # para instalar o pip3
sudo rm /usr/bin/pip # caso você tenha o pip já instalado
sudo mv /usr/bin/pip3 /usr/bin/pip # apenas para renomear o arquivo e tornálo mais acessivél .....
sudo pip install --upgrade pip # atualizar para a última versão do gerenciador pip """
import requests
#Beautiful Soup 4 BS4 pip install bs4 -> para trabalhar com pagina web

cabecalho = {'User-agent': 'Windows 14',
              'Referer': 'https://google.com.br',
              'CF-IPcountry': 'US'}
meus_cookies = {'Ultima-visita': '10-10-2021'}
dados={'username': 'oioi',
        'password': 'oioi123'}
site = 'https://putsreq.com/aajiYq89iy9dHHA94wLv'
text = None

try:
  requisicao = requests.post(site,
    headers=cabecalho,
    cookies=meus_cookies,
    data=dados)
  text = requisicao.text
except Exception as e:
  print("Requisicao deu erro:", e)

print(text)