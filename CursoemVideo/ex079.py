lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resp = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*30)
lista.sort()
print(f'Os valores adicionados foram {lista}')

