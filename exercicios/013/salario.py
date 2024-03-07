salario = float(input('Informe seu salário atual: '))
porcentagemAumento = 0.15
valorAumento = salario * porcentagemAumento
salarioAtualizado = salario + valorAumento

print('O seu novo salário será de R${:.2f} reais' .format(salarioAtualizado))