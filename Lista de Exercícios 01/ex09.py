km = float(input('Quantos Km foram rodados com o carro: '))
dia = int(input('Quantos dias o carro foi utilizado: '))
preco_dia = dia * 60
preco_km = km * 0.15
total = preco_dia + preco_km
print(f'Com {dia} utilizado(s) e {km} rodados. O valor total do carro alugado é de R${total:.2f}')