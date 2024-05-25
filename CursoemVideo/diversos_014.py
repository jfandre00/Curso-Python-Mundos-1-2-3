#saber se o ano é bissexto

ano = int(input('Digite o ano para saber se é bissexto: '))

if ano % 4 == 0:
    if ano %100 == 0 and ano %400 == 0:
        print('É bissexto')
    elif ano %100 == 0 or ano %400 == 0:
        print('Não é bissexto!')
    else:
        print('É bissexto')
else:
    print('Não é bissexto!')
