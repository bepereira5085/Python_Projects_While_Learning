try:
    print('')
    print('FATOS DO NOME SEU E IDADE')
    print('')

    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    print('')

    if nome and idade:

        print(f'Seu nome é {nome}')
        print(f'Seu nome invertido é {nome[::-1]}')
        if ' ' in nome:
            print(f'Seu nome tem espaço(s)')
        else:
            print('Seu nome não tem espaços')
        print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A última letra do seu nome é {nome[-1]}')
    else:
        print('Por favor, digite nome e idade')
except:
    print('ERRO, TENTE NOVAMENTE!')