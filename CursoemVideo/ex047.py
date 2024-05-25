for contador in range (1,51):
    if contador%2 == 0:
        print(contador, end=' ')
print('Acabou')

# outra opção

for contador in range (2, 51, 2):
    print(contador, end=' ')

#no caso acima faz metade das iterações. Ocupa menos processador, mais leve.
