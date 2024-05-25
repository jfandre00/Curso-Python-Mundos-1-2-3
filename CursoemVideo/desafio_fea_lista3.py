from random import randint
def sortear_bingo():
    numeros_sorteados = list()
    cont_c1 = cont_c2 = 0
#Daqui pra baixo comecam os sorteios e a conferencia se o número já não foi sorteado
    while True:
        sorteio = str(input('Pressione ENTER para sortear um número [qualquer tecla para parar]: '))
        if sorteio == '':
            randomico = randint(1,20)
            while True:
                if randomico in numeros_sorteados:
                    randomico = randint(1, 20)
                else:
                    break
            numeros_sorteados.append(randomico)
            print(f'Número sorteado: {randomico}')
            if len(numeros_sorteados) == 20: #sai do loop caso já tenha sorteado os 20 numeros, senão travaria
                print('B I N G O ! ! ! ! ! !') #significa que deu bingo no último sorteio
                break
        else:
            break
#Daqui pra baixo vamos conferir se o numero sorteado está na cartela e marca um X se está:
        if randomico in cartela[0]:
            i = cartela[0].index(randomico)
            cartela[0][i] = 'X'
            cont_c1 += 1
        if randomico in cartela[1]:
            i = cartela[1].index(randomico)
            cartela[1][i] = 'X'
            cont_c2 += 1
        if cont_c1 == 5 and cont_c2 == 5: #significa que a cartela está completa
            print('B I N G O ! ! ! ! ! !')
            print(f'Sua cartela:\n{cartela[0]}\n{cartela[1]}')
            break
        print(f'Sua cartela:\n{cartela[0]}\n{cartela[1]}')


#Declaração das variáveis globais:
c = 1
cartela_toda  = list()
cartela = list()
c1 = list()
c2 = list()
cartela = [c1, c2]

#Daqui para baixo vou criar a cartela de 2 listas com 5 elementos cada:
while c <= 10:
    randomico = randint(1, 20)
    while True:
        if randomico in cartela_toda:
            randomico = randint(1, 20)
        else:
            break
    cartela_toda.append(randomico)
    c += 1
for c in range(0,5):
    c1.append(cartela_toda[c])
for c in range(5,10):
    c2.append(cartela_toda[c])
print(f'Sua cartela:\n{cartela[0]}\n{cartela[1]}')

#Agora vamos chamar o bingo...

sortear_bingo()
