notas = [50, 20, 10, 5, 2, 1]
conta = int(input('Valor da compra: R$ '))
pgto = int(input('Pagamento: R$ '))
troco = pgto - conta
while troco != 0:
    if troco > 0:
        # Para cada nota na lista de notas
        for nota in notas:
            # Se a nota escolhida for maior que o troco, então
            # a nota recebe o valor dela mesma subtraida do valor do troco
            if nota > troco:
               nota -= troco
            # Se o valor da nota é igual o valor do troco, então ok
            if nota == troco:
                print(f'Troco: R$ {nota}')
                troco = 0
    # Se o troco for menor que 0 significa que falta pagamento do cliente
    if troco < 0:
        print(f'\033[31mFalta o cliente realizar o pagamento de\033[m R$ {abs(troco)}')
        pagou = ' '
        while pagou not in 'SN':
            pagou = str(input('Cliente realizou pagamento do valor restante? [S/N] ')).strip().upper()[0]
            # Enquanto cliente não pagou, realiza o loop perguntando do pagamento
            if pagou == 'N':
                print(f'\n\033[31mPor favor realizar pagamento do valor restante!!\033[m')
        # Se o cliente pagou, confirma qual foi o valor pago
        if pagou == 'S':
            pgto = int(input('Valor recebido: R$ '))
            # Se o valor pago for igual ao troco, então ok e saí do loop
            if pgto == abs(troco):
                print('\033[32mMuito obrigado!! Volte Sempre!\033[m')
                break
        # Se o valor pago for menor do que o esperado, calcula o restante e pergunta novamente
        if pgto < abs(troco):
            rest = abs(pgto - abs(troco))
            print(f'\033[31mAinda falta realizar o pagamento de\033[m R$ {rest}')
            pgto = int(input('Valor recebido: R$ '))
            # Se o valor esperado foi pago, então ok
            if pgto == rest:
                print('\033[32mMuito obrigado!! Volte Sempre!\033[m')
                break
            # Se o cliente pagou a mais que o valor esperado então calcula o troco
            if pgto > rest:
                troco = pgto - rest
                for nota in notas:
                    if nota > troco:
                        nota -= troco
                    if nota == troco:
                        print(f'\nTroco: R$ {nota}')
                break
print('\033[32mMuito Obrigado. Volte Sempre!!!\033[m')