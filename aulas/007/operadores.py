num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
s = num1 + num2
m = num1 * num2
d = num1 / num2
di = num1 // num2
e = num1 ** num2

print('A soma é {} o produto é {} e a divisão é {:.2f}' .format(s, m, d))
print('Divisão inteira é {} e a potencia é {}' .format(di, e))