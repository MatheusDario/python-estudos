nome = str(input('Informe seu nome completo: '))
print(nome.upper())
print(nome.lower())
novoNome = nome.replace(' ', '')
print(novoNome)
print(len(novoNome))
primeiroNome = nome.split(' ')
print(primeiroNome[0])