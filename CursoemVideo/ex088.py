from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('JOGA NA MEGA SENA'.center(30))
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print("-="*3, f' SORTEANDO {quant} JOGOS ', '-='*3)
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}')
    sleep(1)
print('-=' *5, '< BOA SORTE >', '-=' *5)

