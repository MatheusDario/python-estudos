num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = 0

if num1 > num2:
  maior = num1
if num1 > num3:
  maior = num1
if num2 > num1:
  maior = num2
if num3 > num1:
  maior = num3
if num3 > num2:
  maior = num3

print('O maior número é o {}' .format(maior))
