nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maíusculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
espaco = nome.count(' ')
compr = len(nome)
letras = compr - espaco
print('Seu nome tem ao todo {} letras (sem considerar os espaços)'.format(letras))
#procuro a posição do primeiro espaco, pois o nome vem antes dele
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

