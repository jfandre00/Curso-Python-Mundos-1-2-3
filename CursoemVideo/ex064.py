numero = cont = soma = 0
while numero != 999:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        soma = soma
        cont = cont
    else:
        soma += numero
        cont += 1
print(f'A soma dos {cont} números inseridos é {soma}')

###########################################################
# Outra solução

#numero = cont = soma = 0
#numero = int(input('Digite um número [999 para parar]: '))
#while numero != 999:
#       soma += numero
#       cont += 1
#       numero = int(input('Digite um número [999 para parar]: '))
#print(f'A soma dos {cont} números inseridos é {soma}')