from math import factorial
n1 = int(input('Digite um número para calcular seu Fatorial: '))
fat = factorial(n1)
print('O fatorial de {} é {}!'.format(n1, fat))

####################################################################

n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else '=', end= ' ')
    f = f * c
    c -= 1
print('{}'.format(f))
print('---------------------------------------')
print('3º forma de calcular o fatorial - usando o FOR')
n2 = int(input('Digite um número para calcular seu Fatorial: '))

fator = 1
for t in range (1, n2+1):
    fator = fator*t
print(fator)
