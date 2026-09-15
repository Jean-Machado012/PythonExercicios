while True:
    usuario = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite sua senha: '))
    if usuario.upper() == senha.upper():
        print('\033[31mNão é perimitido senha igual ou similar ao nome de usuário.\033[m')
        print('\033[31mTente novamente.\033[m')
    else:
        print('Usuário cadastrado com sucesso')
        break