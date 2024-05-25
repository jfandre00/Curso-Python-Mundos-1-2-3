num = int(input('Informe um número: '))
u = num // 1 %10
d = num // 10 %10
c = num // 100 %10
m = num // 1000 %10
print('Analisando o número {}'.format (num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))

#exemplo numero 1255
#u = 1256 divido por 1 = 1256, divido por 10 = 125 resta 6, que é a unidade
#d = 1256 divido por 10 = 125, dividido por 10 = 12 resta 5, que é a dezena
#c = 1256 divido por 100 = 12, dividido por 10 = 1 resta 2, que é a centena
#m = 1256 divido por 1000 = 1, dividido por 10 = 0 resta 1, que é o milhar

