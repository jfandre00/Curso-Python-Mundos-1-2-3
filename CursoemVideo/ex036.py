casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar?: '))

prestacao_mensal = casa / (anos * 12)
if prestacao_mensal <= 0.30 * salario:
    print('Empréstimo Aprovado!!!')
    print(f'Para comprar uma casa de R${casa:.2f} em {anos} anos, o valor da prestação mensal é R${prestacao_mensal:.2f}')
else:
    print(f'Infelizmente seu financiamento não será aprovado.', end=' ')
    print(f'A prestação mensal é R${prestacao_mensal:.2f} e a sua capacidade de pagamento é {0.3*salario:.2f}!')