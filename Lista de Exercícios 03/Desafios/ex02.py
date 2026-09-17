notas = [50, 20, 10, 5, 2, 1]
conta = int(input('Valor da compra: R$ '))
pgto = int(input('Pagamento: R$ '))
troco = pgto - conta
while troco != 0:
    if troco > 0:
        for nota in notas:
            if nota > troco:
               nota -= troco
            if nota == troco:
                print(f'Troco: R$ {nota}')
                troco = 0
    if troco < 0:
        print(f'\033[31mFalta o cliente realizar o pagamento de\033[m R$ {abs(troco)}')
        pagou = ' '
        while pagou not in 'SN':
            pagou = str(input('Cliente realizou pagamento do valor restante? [S/N] ')).strip().upper()[0]
            if pagou == 'N':
                print(f'\n\033[31mPor favor realizar pagamento do valor restante!!\033[m')
        if pagou == 'S':
            pgto = int(input('Valor recebido: R$ '))
            if pgto == abs(troco):
                print('\033[32mMuito obrigado!! Volte Sempre!\033[m')
                break
        if pgto < abs(troco):
            rest = abs(pgto - abs(troco))
            print(f'\033[31mAinda falta realizar o pagamento de\033[m R$ {rest}')
            pgto = int(input('Valor recebido: R$ '))
            if pgto == rest:
                print('\033[32mMuito obrigado!! Volte Sempre!\033[m')
                break
            if pgto > rest:
                troco = pgto - rest
                for nota in notas:
                    if nota > troco:
                        nota -= troco
                    if nota == troco:
                        print(f'\nTroco: R$ {nota}')
                break
print('\033[32mMuito Obrigado. Volte Sempre!!!\033[m')