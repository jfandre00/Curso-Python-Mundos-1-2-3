opcao = 'S'
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    if opcao == 'N':
        print('Obrigado por utilizar o programa! Tchau!')
        break
    elif opcao == 'S':
        while True:
            num = int(input('Digite um número entre 0 a 20: '))
            if num not in range(0, 21):
                # poderia fazer também 0 <= num <= 20: (no if)
                print('Tente Novamente!', end=' ')
            else:
                break
        print(f'Você digitou o número {cont[num]}!')
        opcao = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]

    else:
        print('Opção Inválida! Tente novamente!')
        opcao = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]

