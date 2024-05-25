dist = float(input('Qual é a distância da sua viagem?: '))
if dist <= 200:
    preco = dist*0.50
else:
    preco = dist*0.45

preco2 = (dist*0.50 if dist <= 200 else dist*0.45)

print('E o preço da sua passagem será R${:.2f}'.format(preco))
print('O preço com if simplificado: R${:.2f}'.format(preco2))
