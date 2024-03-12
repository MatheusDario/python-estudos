frase = str(input('Digite uma frase: ')).upper().strip()
print('Quantas vezes aparece a letra A, {} vezes' .format(frase.count('A')))
print('A primeira letra A apareceu na posiçao: {}' .format(frase.find('A')+ 1 ))
print('A última aparição da letra A foi na posição: {}' .format(frase.rfind('A')+ 1))