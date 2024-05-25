'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão
no intervalo compreendido por eles e mostre a soma entre os números.
'''

def somar(menor, maior):
    soma = 0
    for c in range(menor, maior + 1):
        soma += c
        print(c, end="...")
    print()
    return soma


n1 = int(input('Primeiro número inteiro: '))
n2 = int(input('Segundo número inteiro: '))

if n1 > n2:
    resultado = somar(n2, n1)
    print(f'A soma é {resultado}')
elif n2 > n1:
    resultado = somar(n1, n2)
    print(f'A soma é {resultado}')
else:
    print(f'Os números {n1} e {n2} são iguais - Não há nada entre eles! Sua soma é {n1+n2}.')