cig_dia = int(input('Quantos cigarros por dia fuma? '))
ano_fuma = int(input(f'A quantos anos fuma {cig_dia} cigarros por dia? '))
# Convertendo a quantidade de anos fumados em dias
dias = ano_fuma * 365
# Calculando o total de cigarros fumados pelo total de dias
tot_cig = cig_dia * dias
# Calcula os minutos fumados no total de anos
min_perda = tot_cig * 10
# Dividindo a quantidade de minutos fumados total pela quantidade de minutos do dia
perda_vida = min_perda / 1440
# Esse resultado da um valor float, então realizo a divisão para armazenar o resto da divisão 
restante_min = min_perda % 1440
# Divido por 60 para saber a quantiade de horas restantes
total_hora_rest = int(restante_min / 60)
# Dividido novamente por 60 e agora o resto da divisão corresponde a quantiade de minutos
total_min_rest = restante_min % 60
print(f'''Com {cig_dia} cigarros fumando por dia há {ano_fuma} ano(s). 
Ao todo já perdeu {int(perda_vida)} dias {total_hora_rest} horas e {total_min_rest} minutos de vida''')