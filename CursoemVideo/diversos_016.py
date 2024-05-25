'''Programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.'''

unidade = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dezena = ['zero', 'dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
teens = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

numero = int(input('Entre com um número entre 0 e 99: '))
if numero < 0:
    print('Não faço isso com números menores que 0! Sorry!!! Saindo...')
elif numero < 10:
    print(f'{unidade[numero]}')
elif numero < 20:
    n = numero - 10
    print(f'{teens[n]}')
elif numero > 99:
    print('Não faço isso com números maiores que 99! Sorry!!! Saindo...')
else:
    deze = numero // 10
    unid = numero - (10*deze)
    print(f'O número {numero} se escreve: {dezena[deze]} e {unidade[unid]}')