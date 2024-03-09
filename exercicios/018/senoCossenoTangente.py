import math

angulo = int(input('Informe o angulo: '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print('O valor do seno é {:.2f}, cosseno {:.2f} e a tangente {:.2f} referente ao Angulo {}' .format(seno, cosseno, tangente, angulo))
