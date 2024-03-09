from math import hypot

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print('O comprimento da hipotenusa é: {:.2f}' .format(hipotenusa))