from random import randint

num = randint(0, 5)
numEscolhido = int(input('Digite o número escolhido pelo computador: '))
if num == numEscolhido:
  print('Você acertou!')
else:
  print('O número escolhido foi {}' .format(num))
