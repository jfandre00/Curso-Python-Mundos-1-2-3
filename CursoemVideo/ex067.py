
while True:
    print('-'*40)
    tabuada = int(input('Quer ver a tabuada de qual valor?: '))
    print('-' * 40)
    if tabuada < 0:
        print('Obrigado por usar o programa!')
        break
    print(f'Tabuada do {tabuada}:')
    for c in range (1,11):
        print(f'{tabuada} x {c} = {tabuada*c}')
