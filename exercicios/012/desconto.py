precoProduto = float(input('Informe o preço do produto: '))
porcentagemDesconto = 0.05
valorDesconto = precoProduto * porcentagemDesconto
produtoDesconto = precoProduto - valorDesconto

print('O preço do produto com desconto será R${:.2f} reais' .format(produtoDesconto))