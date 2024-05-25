''' Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 '''

inteiro = int(input('Entre com um número inteiro positivo menor que 1.000: '))
if inteiro > 999:
    print('Número fora do alcance do programa! Saindo...')
elif inteiro < 1:
    print('Número abaixo do alcance do programa! Saindo...')
else:
    centenas = inteiro // 100
    if centenas == 0:
        cent = ''
    elif centenas == 1:
        cent = 'centena'
    else:
        cent = 'centenas'
    dezenas = (inteiro - (100*centenas)) // 10
    if dezenas == 0:
        deze = ''
    elif dezenas == 1:
        deze = 'dezena'
    else:
        deze = 'dezenas'
    unidades = (inteiro - (100*centenas) - (10*dezenas))
    if unidades == 0:
        unid = ''
    elif unidades == 1:
        unid = 'unidade'
    else:
        unid = 'unidades'
if centenas == 0:
    if dezenas == 0:
        print(f'{unidades} {unid}')
    else:
        if unidades == 0:
            print(f'{dezenas} {deze}')
        else:
            print(f'{dezenas} {deze} e {unidades} {unid}')
if centenas != 0:
    if unidades == 0 and dezenas == 0:
        print(f'{centenas} {cent}')
    elif unidades == 0 and dezenas != 0:
        print(f'{centenas} {cent} e {dezenas} {deze}')
    elif unidades != 0 and dezenas == 0:
        print(f'{centenas} {cent} e {unidades} {unid}')
    else:
        print(f'{centenas} {cent}, {dezenas} {deze} e {unidades} {unid}')
