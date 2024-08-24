try:
    print('')
    print('FATOS DO SEU NOME E IDADE')
    print('')

    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    idade = int(idade)
    print('')

    if nome and idade:

        print(f'Seu nome é {nome}')
        if idade >= 18:
            print('Você é maior de idade')
        else:
            print('Você é menor de idade')
        print(f'Seu nome invertido é {nome[::-1]}')
        if ' ' in nome:
            print(f'Seu nome tem espaço(s)')
        else:
            print('Seu nome não tem espaços')
        if ' ' in nome:
            print('Seu nome é composto')
            espacos = nome.count(' ')
            print(f'Seu nome tem {len(nome) - espacos} letras')
        else:
            print('Seu nome não é composto')
            print(f'Seu nome tem {len(nome)} letras')
        print(f'A primeira letra do seu nome é {nome[0]}')
        print(f'A última letra do seu nome é {nome.upper()[-1]}')
    else:
        print('Por favor, digite nome e idade')
except:
    print('ERRO, TENTE NOVAMENTE!')
