n1 = int(input('\033[4mPrimeiro Número\033[m: '))
n2 = int(input('\033[4mSegundo Número\033[m: '))
if n1 > n2:
    print(f'O Primeiro número, {n1}, é maior do que o Segundo número, {n2}.')
elif n2 > n1:
    print(f'O Segundo número, {n2}, é maior do que o Primeiro número, {n1}.')
else:
    print(f'{n1} e {n2} são iguais.')
