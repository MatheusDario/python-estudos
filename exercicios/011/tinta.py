altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area = largura * altura
litroTinta = area / 2

print('Uma parede de {}m de altura e {}m de largura tem {}m quadrados e será nescessário {} litros de tinta' .format(altura, largura, area, litroTinta))