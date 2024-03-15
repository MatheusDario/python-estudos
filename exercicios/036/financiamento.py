valorCasa = int(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Em quantos anos deseja parcelar ? '))

meses = anos * 12
valorMensal = valorCasa / meses
margem = salario * 0.30
if valorMensal > margem:
  print('Não será possível realizar o financiamento') 

print('O valor da prestação será {:.2f}' .format(valorMensal))