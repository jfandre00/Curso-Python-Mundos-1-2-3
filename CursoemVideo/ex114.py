import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.uol.com.br')
except:
    print('Deu Erro')
else:
    print('Tudo ok')
