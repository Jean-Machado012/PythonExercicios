salario = float(input('Digite seu salário: R$ '))
aumento = float(input('Digite a porcentagem de aumento: '))
valor_aumento = (aumento/100) * salario
novo_salario = valor_aumento + salario
print(f'O valor de aumento será de R$ {valor_aumento:.2f}, ou seja, o salário total vai ser de R$ {novo_salario:.2f}')