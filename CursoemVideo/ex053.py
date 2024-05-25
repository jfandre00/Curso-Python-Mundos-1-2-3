frase = str(input('Escreva a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

'''
#irá da ultima letra (comprimento do junto -1) ate a primeira (-1), voltando uma letra (-1)
for letra in range(len(junto) -1, -1, -1):
    inverso = inverso + junto[letra]'''

# abaixo o método mais simples que só funciona em python - FATIAMENTO
inverso = junto[::-1]
# pega do início ao fim e inverte
# ###########################

print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')

