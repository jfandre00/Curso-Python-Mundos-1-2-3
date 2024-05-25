#Conversão de temperaturas C e F
celsius = float(input('Qual é a temperatura em Celsius?: '))
fahrenheit = (celsius *(9/5)) + 32
#pela regra do PEMBAS - não precisaria dos ()
print('A temperatura de {:.2f}ºC corresponde, em Fahrenheit, a {:.2f}F!'.format(celsius, fahrenheit))

#é mais fácil e fica mais bonito - o uso de parênteses!!
