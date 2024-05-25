from datetime import date
atual = date.today().year

cont_maior = 0
cont_menor = 0

for contador in range (1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu?: '.format(contador)))
    idade = atual - nasc
    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1
print('No total temos {} pessoas maiores de idade e {} pessoas menores de idade!'.format(cont_maior, cont_menor))