expressao = str(input('Digite uma expressão: '))
#toda string é uma lista
pilha = []
for cadasimbolo in expressao:
    if cadasimbolo == '(':
        pilha.append('(')
    elif cadasimbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
