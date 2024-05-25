print('='*30)
print('10 TERMOS DE UMA P.A.')
print('='*30)
primeiro = int(input('Entre com o primeiro termo: '))
razao = int(input('Entre com a razão: '))
decimo = primeiro + (10 -1) * razao

for contador in range(primeiro, decimo + razao, razao):
    print('{} '.format(contador), end=' → ')
print('ACABOU!!')

