num = int(input('Digite um número inteiro: '))
print('\033[4mEscolha uma das bases para conversão\033[m:')
print('\033[31m[ 1 ]\033[m converter para BINÁRIO')
print('\033[32m[ 2 ]\033[m converter para OCTAL')
print('\033[33m[ 3 ]\033[m converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Opção Inválida, tente novamente!!')

# o problema é que aparece 0b, 0c e 0x na frente dos números convertidos
# não me importa esse começo, então vamos fazer FATIAMENTO da string
# eu quero remover a posição 0 e 1 dessas strings (0b, 0c, 0x)
# vamos colocar o [2:] depois da chamada da variável