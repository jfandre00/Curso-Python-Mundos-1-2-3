'''Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima
a data com o nome do mês por extenso.

Data de Nascimento: 29/10/1973
Você nasceu em  29 de Outubro de 1973.'''
def bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 == 0:
            return True
        elif ano % 100 == 0 or ano % 400 == 0:
            return False
        else:
            return True
    else:
        return False


meses = [
    'NADA', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro'
]
mes31 = [1, 3, 5, 7, 8, 10, 12]

data = str(input('Digite a data de nascimento no formato dd/mm/aaaa: ')).strip()
if len(data) > 10 or len(data) < 10:
    print('Há algo errado com os dados inseridos. Saindo...')
else:
    mes = data[3:5]
    dia = data[0:2]
    ano = data[6:11]
    if (mes.isnumeric() and dia.isnumeric() and ano.isnumeric() and int(mes) != 0 and
            int(dia) != 0 and int(ano) != 0 and int(mes) <= 12 and int(dia) <= 31):
        if int(mes) == 2:
            b = bissexto(int(ano))
            if int(dia) == 29 and b == True:
                print(f'Você nasceu em {dia} de {meses[int(mes)]} de {ano}')
            elif int(dia) < 29:
                print(f'Você nasceu em {dia} de {meses[int(mes)]} de {ano}')
            else:
                print('Há algo errado com os dados inseridos. Saindo...')
        elif int(dia) == 31 and int(mes) not in mes31:
            print('Há algo errado com os dados inseridos. Saindo...')
        else:
            print(f'Você nasceu em {dia} de {meses[int(mes)]} de {ano}')
    else:
        print('Há algo errado com os dados inseridos. Saindo...')