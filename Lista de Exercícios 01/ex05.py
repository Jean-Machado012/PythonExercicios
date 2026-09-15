preco = float(input('Qual o preço do produto: R$ '))
porcentagem_desconto = float(input('Digite a porcentagem de desconto: '))
desconto = (porcentagem_desconto/100) * preco
valor_final = preco - desconto
print(f'Valor de desconto sobre o produto é de R$ {desconto:.2f}, com o valor total de venda de R$ {valor_final:.2f}')
