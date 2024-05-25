#Jogo de Craps. Faça um programa de implemente um jogo de Craps.
# O jogador lança um par de dados, obtendo um valor entre 2 e 12.
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

from random import randint
from time import sleep

dado1 = randint(1,6)
dado2 = randint(1,6)
jogada = 1
soma = dado1 + dado2
print(f'{jogada}º jogada -> Dado 1: \033[1;35m{dado1}\033[m -> Dado 2: \033[1;35m{dado2}\033[m ->>>> Boa Sorte!')
sleep(2)

while True:
    if jogada == 1 and (soma == 7 or soma == 11):
        print(f'Soma dos dados foi {soma} - Ganhou - Você é um NATURAL')
        break
    elif jogada == 1 and (soma == 2 or soma == 3 or soma == 12):
        print(f'Soma dos dados foi {soma} - Perdeu - CRAPS')
        break
    elif jogada == 1 and (soma == 4 or soma == 5 or soma == 6 or soma == 8 or soma == 9 or soma == 10):
        ponto = soma
        print(f'{ponto} - Esse é seu PONTO')
        sleep(2)
    jogada += 1
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2
    print('-'*30)
    print(f'{jogada}º jogada -> Dado 1: \033[1;35m{dado1}\033[m -> Dado 2: \033[1;35m{dado2}\033[m ->>>> Boa Sorte!')
    print(f'Lembrando, o seu ponto é \033[31m{ponto}\033[m')
    sleep(2)
    if soma == 7:
        print(f'Seus dados somaram {soma} - Perdeu!!')
        break
    if soma == ponto:
        print(f'\033[1;35mParabéns! Você ganhou!! Precisou jogar os dados \033[33m{jogada}\033[1;35m vezes!\033[m')
        break



