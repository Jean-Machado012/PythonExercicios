lista = list()
n1 = int(input('Primeiro número: '))
lista.append(n1)
n2 = int(input('Segundo número: '))
lista.append(n2)
n3 = lista[-2] % lista[-1]
lista.append(n3)
while n3 != 0:
    n3 = lista[-2] % lista[-1]
    lista.append(n3)
print(f'Para os números inteiros {n1} e {n2}, o MDC entre eles é: {lista[-2]}')
print('Conforme o Algoritmo de Euclides!')