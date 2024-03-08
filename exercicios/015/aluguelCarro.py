dias = int(input('Informe quantos dias o carro foi alugado: '))
distancia = float(input('Informe qual foi a distancia percorrida em Km: '))
valorDia = dias * 60
valorKm = distancia * 0.15
total = valorDia + valorKm
print('O total a pagar é R${:.2f}'.format(total))