lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    contin = str(input('Deseja Prosseguir? [S/N]: '))
    if contin in 'Nn':
        break
for indice, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    elif valor % 2 == 1:
        impares.append(valor)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
