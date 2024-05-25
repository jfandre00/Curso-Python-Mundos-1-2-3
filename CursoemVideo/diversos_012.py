nome = str(input('Digite o nome: '))
comp = len(nome)

print('----- IMPRIMINDO O NOME NA VERTICAL -----')
print()
for c in range(0, comp):
    print(nome[c])

print()
print('----- IMPRIMINDO O NOME NA VERTICAL EM ESCADA -----')
r = 0
while r <= comp:
    for c in range(0, r):
        print(nome[c],end='')
    print()
    r += 1
print()
print('----- IMPRIMINDO O NOME NA VERTICAL EM ESCADA INVERTIDA -----')
print()
r = comp
while r >= 0:
    for c in range(0, r):
        print(nome[c],end='')
    print()
    r -= 1