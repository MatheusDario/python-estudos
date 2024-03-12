nome = str(input('Digite seu nome completo: ')).strip()
fname = nome.split()
print('Seu primeiro nome é {}' .format(fname[0]))
print('Seu último nome é {} ' .format(fname[len(fname) - 1]))