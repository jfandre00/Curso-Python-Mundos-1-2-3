soma = 0
con_pares = 0
for cont in range (1, 7):
    num = int(input('Digite um valor: '))
    if num %2 == 0:
        soma += num
        con_pares += 1

print(f'Você informou {con_pares} números pares e a soma foi: {soma}')
