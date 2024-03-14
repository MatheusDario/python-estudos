distancia = int(input('Digita a distancia total da viagem em Km: '))
if distancia > 200:
  preco = distancia * 0.45
  print('O preço da viagem será de {:.2f} reais' .format(preco))
else:
  preco = distancia * 0.50
  print('O preço da viagem será de {:.2f} reais' .format(preco))

