dinheiro = float(input('Quanto dinheiro você tem na carteira?: R$'))
print('US$1.00 equivalem a R$3.27')
dolar = dinheiro / 3.27
euro  = dinheiro / 4.52
print('Você pode comprar US${:.2f}!'.format(dolar))
print('Você pode comprar {:.2f} Euros!'.format(euro))