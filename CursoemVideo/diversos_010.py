'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
1 - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer
    pedir os demais valores, sendo encerrado;
2 - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
3 - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
4 - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

print('Calculador de Equações do 2º Grau')
print('Formato: \033[21;32ma\033[mx² + \033[21;32mb\033[mx + \033[21;32mc\033[m')
a = int(input('Insira o valor de \033[32ma\033[m: '))
if a == 0:
    print('A equação não é do segundo grau. Saindo...')
else:
    b = int(input('Insira o valor de \033[32mb\033[m: '))
    c = int(input('Insira o valor de \033[32mc\033[m: '))
delta = (b*b) - (4*a*c)
if delta < 0:
    print('A equação não possui raízes reais! Saindo...')
elif delta == 0:
    raiz1 = (-b)/(2*a)
    print(f'A equação possui apenas uma raiz e é {raiz1}')
else:
    delta = (b*b) - (4*a*c)
    raizdelta = delta**(1/2)
    raiz1 = (-b + raizdelta)/(2*a)
    raiz2 = (-b - raizdelta)/(2*a)
    print(f'A equação possui duas raízes reais e são {raiz1:.2f} e {raiz2:.2f}')