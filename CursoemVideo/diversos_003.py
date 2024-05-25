#dados 5 numeros inteiros positivos, encontre os valores minimo e maximo que podem ser calculados somando exatamente
#4 dos 5 inteiros. Em seguida, imprima os respectivos valores min e max como uma unica linha de dois inteiros longos
#separados por espaço

from random import randint
lista = []
soma = maior = menor = 0

for c in range(0,5):
    x = randint(1,20)
    while True:
        if x in lista:
            x = randint(1,20)
        else:
            lista.append(x)
            break

print(f'Lista com os números escolhidos: \033[1;33m{lista}\033[m')

for c in range(0,5):
    soma += lista[c]
    if c == 0:
        menor = maior = lista[c]
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]
print(f'O máximo valor somando os 4 maiores é \033[34m{soma-menor}\033[m; O mínimo valor somando os 4 menores é \033[35m{soma-maior}\033[m.')
