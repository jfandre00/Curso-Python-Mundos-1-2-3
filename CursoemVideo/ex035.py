a = '-='
print(a*20)
print('ANALISADOR DE TRIÂNGULOS')
print(a*20)
reta1 = float(input('Coloque o comprimento da primeira reta: '))
reta2 = float(input('Coloque o comprimento da segunda reta: '))
reta3 = float(input('Coloque o comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('É possível fazer um triângulo com essas retas!!!')
else:
    print('Não é possível fazer um triângulo com essas retas!!!')
