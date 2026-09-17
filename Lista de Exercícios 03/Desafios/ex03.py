n = int(input('Digite um número inteiro para verificar se ele é primo: '))
cont = 0
for i in range(1, n + 1):
    if n % i == 0:
        cont += 1
if cont == 2:
    print(f'{n} é um número primo')
else:
    print(f'{n} não é um número primo')