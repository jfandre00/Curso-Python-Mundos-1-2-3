salario = float(input('Qual o salário do funcionário: R$'))
aumento = salario * 15 / 100
novo_salario = salario + aumento
print('O salário de R${:.2f} terá um aumento de 15%, que representa R${:.2f}. Novo salário será R${:.2f}'.format(salario, aumento, novo_salario))

#fazendo um plano de pagamentos

produto = float(input('Qual o valor do produto?: R$'))
avista = produto - (produto * 10 / 100)
# desconto de 10% a vista
debito = produto
crédito = produto + (produto * 5 / 100)
# acréscimo de 5% no crédito
parcelado = produto + (produto * 10 / 100)
# acréscimo de 10% para parcelado

print('O produto que custa R${:.2f} tem as seguintes opções de pagamento: \nÀ Vista : R${:.2f} \nNo Débito : R${:.2f} \nNo Crédito : R${:.2f} \nParcelado : R${:.2f}'.format(produto, avista, debito, crédito, parcelado))