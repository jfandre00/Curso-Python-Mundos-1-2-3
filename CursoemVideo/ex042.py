s1 = int(input('Primeiro Segmento: '))
s2 = int(input('Segundo Segmento: '))
s3 = int(input('Terceiro Segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('É possível formar um triângulo e ele será um', end=' ')
    if s1 == s2 == s3:
        print('Triângulo Equilátero')
    elif s1 != s2 != s3 != s1:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não é possível formar um triângulo com esses segmentos de reta')
