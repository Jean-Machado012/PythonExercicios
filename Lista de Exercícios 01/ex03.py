dias = int(input('Valor em dias: '))
horas = int(input('Valor em horas: '))
minutos = int(input('Valor em minutos: '))
segundos = int(input('Valor em segundos: '))
dias *= 24 * 3600
horas *= 3600
minutos *= 60
total = dias + horas + minutos + segundos
print(f'Total em segundos é igual a {total}')