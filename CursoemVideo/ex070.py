total = tot1000 = menor = cont = 0
barato =' '
while True:
    print('-'*40)
    print('LOJA SUPER BARATÃO'.center(40))
    print('-'*40)
    produto = str(input('Qual é o nome do produto: '))
    preco = float(input('Qual é o preço do produto: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        tot1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja Continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(' FIM DO PROGRAMA '.center(40, '-'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {tot1000} produtos custando mais de R$1.000,00!')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')