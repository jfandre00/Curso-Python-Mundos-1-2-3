from random import randint
aleatorio = (randint(1,10), randint(1,10),
             randint(1,10), randint(1,10),
             randint(1,10))
print(f'Eu sorteei os valores {aleatorio}')
print('Os valores sorteados foram: ',end='')
for elemento in aleatorio:
    print(f'{elemento} ',end='')
print(f'\nO maior valor sorteado foi {max(aleatorio)}')
print(f'O menor valor sorteado foi {min(aleatorio)}')
