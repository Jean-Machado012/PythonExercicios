nota = -1
while nota > 10 or nota < 0:
    nota = float(input('Insira uma nota entre 0 e 10: '))
    if 0 <= nota <= 10:
        print(f'Você deu a nota {nota}')
        break
    else:
        print('\033[31mERRO!!! Insira uma nota entre 0 e 10\033[m')