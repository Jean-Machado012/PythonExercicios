distancia = float(input('Qual a distância da viagem em Quilomêtros (Km)? '))
velocidade = float(input('Qual a velocidade média prevista (Km/H): '))
tempo = distancia / velocidade
horas = int(tempo)
minutos = int((tempo - horas) * 60)
print(f'A quantidade de horas prevista para à viagem é de {horas} horas e {minutos} minutos.')