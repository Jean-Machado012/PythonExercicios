peso = float(input('Quantos Kg pescou? '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Excedeu o limite em {excesso:.2f}Kg. Deverá pagar R${multa:.2f} de multa')
else:
    excesso = 0
    multa = 0
    print(f'Peso dentro do limite, excesso = {excesso}, multa = R${multa}')