# Importante ressaltar que o exercício traz uma outra definição de número triangular
# Segundo o conceito de Aristoteles

n = int(input('Digite um número inteiro para saber se ele é triangular: '))
i = 1
# Seguindo a lógica do exercicio, são necessários vários testes até encontrar
# uma sequência de três números que multiplicados irão dar o valor inserido
# Importante ressaltar que é utilizado o <= porque se utilizar o !=, este loop
# jamais iria parar se o valor da multiplicação não for igual a n
while i * (i + 1) * (i + 2) <= n:
    # Multiplicando os números sequencias começando do 1
    mult = i * (i + 1) * (i + 2)
    # Realizando verificação...
    if mult == n:
        print(f'{i} x {i +1} x {i + 2} = {mult}')
        print(f'{n} é um número triangular')
        break
    i += 1
else:
    print(f'{n} não é um número triangular')