cont = soma = 0
while True:
    valor = int(input('Digite o valor (999 para parar): '))
    if valor == 999: #estou verificando antes de somar e contar
        break
    cont = cont + 1
    soma = soma + valor
print(f'Você digitou {cont} números e sua soma é {soma}')