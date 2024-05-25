lista = []
while True:
    lista.append(int(input('Digite um valor?: ')))
    resp = str(input('Deseja Continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Foram Digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')