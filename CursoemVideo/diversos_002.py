from random import randint
resp = 'S'
while True:
    if resp == 'N' :
        print('Tchau!!!')
        break
    if resp not in 'S':
        print('Erro! Digite Novamente S ou N!')
    if resp == 'S':
        comp = randint(0, 10)
        pontuacao = 100
        tent = 1
        print(f'Palpite do computador: {comp}') #esconder essa linha no jogo
        while True:
            palpite = int(input(f'Digite a {tent}º tentativa: '))
            if palpite not in range(0, 11):
                print('ERRO! Fora do Alcance! Digite Novamente!!')
            elif palpite == comp:
                if tent == 5:
                    print(f'Você adivinhou em {tent} tentativas!!, sua pontuação foi 10!')
                    break
                print(f'Você adivinhou em {tent} tentativas!!, sua pontuação foi {pontuacao}!!')
                break
            else:
                pontuacao -= 25
                tent += 1
            if tent == 6:
                break
        if palpite != comp:
            print('Você não acertou nas 5 tentativas e não fez nenhum ponto!')
    resp = str(input('Deseja Jogar novamente? [S/N]: ')).upper().strip()[0]