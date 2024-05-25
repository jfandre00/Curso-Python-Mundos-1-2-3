frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes (independente de maiúsculo ou minúsculo)'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
#aonde aparece a última ocorrência de A
#use o rfind para comecar a procurar da direita para a esquerda
print('A última letra "A" apareceu na posição {}'.format(frase.rfind('A')+1))