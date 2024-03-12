def sauda(nome):
  print('Olá, {} !' .format(nome))
  sauda2(nome)
  print('Preparando para dizer tchau...')
  tchau()

def sauda2(nome):
  print('Como vai {} ?' .format(nome))

def tchau():
  print('Ok, tchau!')

sauda2('Matheus Dario')
sauda('Matheus Dario')