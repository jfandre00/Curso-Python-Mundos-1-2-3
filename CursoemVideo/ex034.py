salario = float(input('Qual é o salário atual do funcionário? R$'))
if salario > 1250.00:
    print('O novo salário terá um aumento de 10%, e será de R${:.2f}'.format(salario + (salario * 10/100)))
else:
    print('O novo salário terá um aumento de 15%, e será de R${:.2f}'.format(salario + (salario * 15/100)))
