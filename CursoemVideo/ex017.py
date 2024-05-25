#poderia fazer também -> math import -> e usar a função math.hypot(oposto, adjacente)

from math import hypot
oposto = float(input('Insira o comprimento do cateto oposto do triângulo: '))
adjacente = float(input('Insira o comprimento do cateto adjacente do triângulo: '))
hipotenusa = hypot(oposto, adjacente)
hipotenusa_matematicamente = ((oposto**2) + (adjacente**2))**(1/2)
print('O comprimento da hipotenusa (calculado pela formula pronta) é {:.2f}'.format(hipotenusa))
print('O comprimento da hipotenusa (calculado matematicamente) é {:.2f}'.format(hipotenusa_matematicamente))