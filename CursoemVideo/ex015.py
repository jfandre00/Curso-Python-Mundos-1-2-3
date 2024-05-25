#Quantos dias alugados 60 / quantos 0,15 km -> valor do aluguel

dias = int(input('Quantos dias o carro foi alugado?: '))
km = float(input('Quantos Kilômetros você rodou?: '))
preco = (dias*60) + (km*0.15)
print('O total da locação foi de R${:.2f}'.format(preco))
