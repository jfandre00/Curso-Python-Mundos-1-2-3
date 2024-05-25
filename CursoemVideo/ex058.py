from random import randint
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue acertar?')
computador = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite?: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez!')
        elif jogador > computador:
            print('Menos... Tente mais uma vez!')

print('Acertou com {} tentativas! Parabéns!'.format(palpites))