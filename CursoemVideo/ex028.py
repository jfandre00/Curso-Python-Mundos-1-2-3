from random import randint
from time import sleep
a ="-=-"
computador = randint(0,5)
print(a*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print(a*20)
num = int(input('Em que número eu pensei? '))
print('Processando ...')
sleep(2)
if num == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador,  num))
