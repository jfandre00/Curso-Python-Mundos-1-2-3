from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja saber: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo {}º tem como Seno {:.2f}, Cosseno {:.2f} e Tangente {:.2f}'.format(angulo,seno,cosseno,tangente))