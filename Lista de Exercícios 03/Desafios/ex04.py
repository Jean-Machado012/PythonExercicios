lista = list()
n = int(input('Digite um número: '))
# Armazenando o valor inserido
lista.append(n)
# Criando um laço for para cada fator iterado iniciando do 2
for fator in range(2, n + 1):
    # Enquanto o resto de n dividido pela iteração for 0
    # mostra o valor da iteração
    while n % fator == 0:
        print(fator, end = ' = ' if fator == n else ' x ')
        # n assume um novo valor. O valor inicial inserido
        # dividido pela iteração
        n = n / fator
print(lista[0])
