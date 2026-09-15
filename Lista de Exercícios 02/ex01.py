lados_triangulo = list()
l1 = float(input('Digite o 1º lado: '))
lados_triangulo.append(l1)
l2 = float(input('Digite o 2º lado: '))
lados_triangulo.append(l2)
l3 = float(input('Digite o 3º lado: '))
lados_triangulo.append(l3)
max = max(lados_triangulo)
soma = sum(lados_triangulo) - max
if soma > max:
    if l1 == l2 == l3:
        print('Triângulo Equilátero')
    elif l1 != l2 != l3:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isoscéles')
else:
    print('Esses lados não formam um triângulo')