from datetime import datetime
nascimento = int(input('Ano de Nascimento: '))
ano_atual = datetime.today().year
idade = ano_atual - nascimento
if idade <= 17:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')
    print(f'Ainda faltam {18-idade} anos para o alistamento')
    print(f'Seu alistamento será em {nascimento+18}')
if idade == 18:
    print(f'Você tem {idade} anos e deve ser alistar IMEDIATAMENTE!!')
if idade > 18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}')
    print(f'Já se passaram {idade-18} anos desde que você deveria ter se alistado!')
    print(f'Você deveria ter se alistado em {nascimento+18}!')
