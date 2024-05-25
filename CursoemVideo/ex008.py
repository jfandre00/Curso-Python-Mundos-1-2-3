valor_m = float(input('Insira um valor em metros (m): '))
print('Convertendo ...')
print('{:.2f}m equivalem a {:.2f}cm'.format(valor_m, valor_m*100))
print('{:.2f}m equivalem a {:.2f}mm'.format(valor_m, valor_m*1000))
# mostrando em tbm km, hectometros, decametros, decimetros
valor_km = valor_m / 1000
valor_hm = valor_m / 100
valor_dm = valor_m / 10
valor_decimetro = valor_m * 10
print('... mais conversões úteis!! ...')
print('{:.2f}m equivalem a {:.3f}km / {:.3f}hm / {:.3f}dm / {:.2f}dcm'.format(valor_m, valor_km, valor_hm, valor_dm, valor_decimetro))