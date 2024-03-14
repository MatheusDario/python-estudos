velocidade = int(input('Digite a velocidade do carro em KM/H: '))

if velocidade > 80:
  multa = (velocidade - 80) * 7
  print('Você foi multado e deverá pagar {},00 reais' .format(multa))
else:
  print('Sua velocidade é {} km/h dirija com cuidado!' .format(velocidade))