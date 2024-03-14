salario = float(input('Digite seu salário atual: '))
if salario > 1250.00:
  aumento = salario * 0.10
  novoSalario = salario + aumento
  print('Seu salário teve um aumento de 10 porcento seu novo valor é {}' .format(novoSalario))
else:
  aumento = salario * 0.15
  novoSalario = salario + aumento
  print('Seu salário teve um aumento de 15 porcento seu novo valor é {}' .format(novoSalario))