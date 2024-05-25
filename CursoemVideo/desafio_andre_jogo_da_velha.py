def tabuleiro():
    print(f'{velha[0]:2} | {velha[1]:2} | {velha[2]:2}\n'
          f'---|----|----\n'
          f'{velha[3]:2} | {velha[4]:2} | {velha[5]:2}\n'
          f'---|----|----\n'
          f'{velha[6]:2} | {velha[7]:2} | {velha[8]:2}')


def vitoria():
    if velha[0] == velha[1] == velha[2] or velha[0] == velha[4] == velha[8] or velha[3] == velha[4] == velha[5]:
        return True
    if velha[6] == velha[7] == velha[8] or velha[6] == velha[4] == velha[2] or velha[0] == velha[3] == velha[6]:
        return True
    if velha[1] == velha[4] == velha[7] or velha[2] == velha[5] == velha[8]:
        return True


def deu_velha():
    contador = 0
    for c in range(0,9):
        if velha[c] == 'X':
            contador += 1
        if velha[c] == 'O':
            contador += 1
    if contador == 9:
        print('Deu Velha')
        return True



#Programa Principal
velha = []
for c in range(1,10):
    velha.append(c)
tabuleiro()
while True:
    x = int(input('Escolha uma posição para colocar o X: '))
    while True:
        if velha[x-1] == 'X':
            print('Esse número já foi escolhido! Tente Novamente')
            x = int(input('Escolha uma posição para colocar o X: '))
        elif velha[x-1] == 'O':
            print('Esse número já foi escolhido! Tente Novamente')
            x = int(input('Escolha uma posição para colocar o X: '))
        else:
            velha[x-1] = 'X'
            break
    if vitoria() == True:
        print(f'Parabéns, o "X" venceu!!')
        tabuleiro()
        break
    if deu_velha() == True:
        break
    tabuleiro()
    while True:
        o = int(input('Escolha uma posição para colocar o O: '))
        if velha[o-1] == 'X':
            print('Esse número já foi escolhido! Tente Novamente')
            o = int(input('Escolha uma posição para colocar o O: '))
        elif velha[x-1] == 'O':
            print('Esse número já foi escolhido! Tente Novamente')
            o = int(input('Escolha uma posição para colocar o O: '))
        else:
            velha[o-1] = 'O'
            break
    tabuleiro()
    if vitoria() == True:
        print(f'Parabéns, o "O" venceu!!')
        tabuleiro()
        break
    if deu_velha() == True:
        break

