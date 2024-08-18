try:
    nome = input('Insira seu nome: ')
    hora = input('Informe a hora atual: ')

    hora = hora[0:2]
    hora_int = int(hora)

    bom_dia = hora_int >= 0 and hora_int <= 11
    boa_tarde = hora_int >= 12 and hora_int <= 17
    boa_noite = hora_int >= 18 and hora_int <= 23

    if bom_dia:
        print(f'Bom dia, {nome}')
    elif boa_tarde:
        print(f'Boa tarde, {nome}')
    elif boa_noite:
        print(f'Boa noite, {nome}')
    else:
        print('O número informado não se refere às horas')

except:
    print('Por favor, digite um número e nome')
