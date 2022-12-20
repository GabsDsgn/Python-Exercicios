import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.erro.URLerror:
    print('O site Pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso')
