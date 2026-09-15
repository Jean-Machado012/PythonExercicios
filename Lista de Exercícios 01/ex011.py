import sys

# Devido a contagem do número ultrapassar o padrão estabelecido pelo Python
# Foi necessário alterar o limite de contagem padrão. Alterado para sem limite.

sys.set_int_max_str_digits(0)
x = pow(2, 10000000)
print(f'{len(str(x))}')