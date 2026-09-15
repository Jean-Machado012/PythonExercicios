sl_hora = float(input('Informe quanto ganha por hora: R$ '))
horas_trab = int(input('Horas trabalhadas no mês: '))
salario = sl_hora * horas_trab
imp_r = (salario * 0.11)
inss = (salario * 0.08)
sind = (salario * 0.05)
descontos = imp_r + inss + sind
salario_bruto = salario + descontos
print(f'''Salário Bruto: R$ {salario_bruto:.2f}
Imposto de Renda: R$ {imp_r:.2f}
INSS: R$ {inss:.2f}
Sindicato: R$ {sind:.2f}
Salário Líquido: R$ {salario:.2f}''')