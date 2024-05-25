preco = float(input('Entre com o preço do produto: R$'))
desconto = preco * 5 / 100
novo_preco = preco - desconto
print('O produto de R${}, com o desconto de (5%) R${:.2f}, passará a custar R${:.2f}'.format(preco, desconto, novo_preco))