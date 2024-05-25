#primeira forma de resolver - importando toda a biblioteca MATH
'''import math
numero = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(numero, math.trunc(numero)))
print('O numero {} tem a parte inteira {}'.format(numero, trunc(numero)))'''

#segunda forma de resolver - importando somente a função TRUNC de dentro de math
'''from math import trunc
numero = float(input('Digite um valor: '))
print('O numero {} tem a parte inteira {}'.format(numero, trunc(numero)))'''

#terceira forma de resolver - direto
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
