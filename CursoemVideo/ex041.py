from datetime import date
nascimento = int(input('Qual seu ano de nascimento?: '))
ano_atual = date.today().year
idade = ano_atual - nascimento
print('O Atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')