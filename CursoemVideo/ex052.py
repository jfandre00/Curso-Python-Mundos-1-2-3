cont_primo = 0
numero = int(input('Digite um número: '))
for contador in range(1, numero+1):
    if numero%contador == 0:
        cont_primo += 1
        print('\033[33m{}\033[m'.format(contador),end=" ")
    else:
        print('\033[31m{}\033[m'.format(contador),end=" ")
print()
if cont_primo == 2:
    print('O número {} foi divisível {} vezes\nE por isso ele é PRIMO!'.format(numero, cont_primo))
else:
    print('O número {} foi divisível {} vezes\nE por isso ele não é PRIMO!'.format(numero, cont_primo))
