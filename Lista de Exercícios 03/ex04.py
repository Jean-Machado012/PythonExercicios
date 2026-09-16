lista = list()
n = int(input('Quantos números de Fibonacci quer mostrar? '))
cont = 3
t1 = 1
t2 = 1
print(f'{t1} -> {t2}', end = '')
while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end = '')
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')