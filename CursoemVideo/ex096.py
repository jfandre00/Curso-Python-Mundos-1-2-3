def area(l, c):
    a = l*c
    print(f'A área de um terreno de {l:.2f}m por {c:.2f}m é de {a:.2f}m².')


#Programa Principal
print('Controle de Terrenos')
print('-'*20)
largura = float(input('Qual é a largura do terreno (m): '))
comprimento = float(input('Qual é o comprimento do terreno (m): '))
area(largura,comprimento)