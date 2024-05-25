peso = float(input('Qual é o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura * altura)
print('O I.M.C. dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif imc <= 25.0:
    print('Peso Ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade Mórbida')