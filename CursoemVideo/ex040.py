n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('Sua Média foi {:.1f} e você está Reprovado'.format(media))
elif media >= 7.0:
    print('Sua Média foi {:.1f} e você está Aprovado'.format(media))
else:
    # poderia ter usado também if 7 > media >= 5:
    # ou ainda if media >= 5 and media <7:
    print('Sua Média foi {:.1f} e você está em Recuperação'.format(media))
