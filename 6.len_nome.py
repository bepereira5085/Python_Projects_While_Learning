try:
    nome = input('Insira seu nome: ')

    curto = len(nome) <= 4
    normal = len(nome) > 4 and len(nome) < 7
    longo = len(nome) > 6

    if curto and nome.isalpha():
        print('Seu nome é curto')
    elif normal and nome.isalpha():
        print('Seu nome é normal')
    elif longo and nome.isalpha():
        print('Seu nome é muito longo')
    else:
        print('Digite um nome apenas com letras e sem espaços')
except:
    print('ERRO')

