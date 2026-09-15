area = float(input('Área a ser pintada (m²): '))
lata = area / 54
if area % 54 != 0:
    lata += 1
preco = int(lata) * 80

print(f'{int(lata)} lata(s) precisa(rão) ser comprada(s), no valor de R$ {preco:.2f}')
