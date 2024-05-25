cont = 0
soma = 0

for numeros in range (1, 501, 2):
    if numeros %3 == 0:
        cont = cont + 1
        soma = soma + numeros

print(f'Existem {cont} números no intervalo')
print(f'A soma de todos esses números é {soma}')
