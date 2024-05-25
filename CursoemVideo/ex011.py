largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Essa parede tem {:.2f}m². Serão necessários {:.2f} litros de tinta para pintá-la!'.format(area, tinta))