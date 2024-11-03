import os
import random

def primeiro_dig(cpf):
    nmr = 10
    soma = 0

    for i in cpf[:9]:
        
        soma += int(i) * (nmr)
        nmr -= 1

    soma *= 10
    resto = soma % 11

    return resto

def segundo_dig(cpf):
    nmr = 11
    soma = 0

    for i in cpf[:10]:
        
        soma += int(i) * (nmr)
        nmr -= 1

    soma *= 10
    resto2 = soma % 11

    return resto2

while True:

    print('GERADOR DE CPF')

    iniciar = input('Digite [1] para gerar um CPF ou\n[0] para sair: ')
    os.system('cls')

    if iniciar != '1' and iniciar != '0':
        print(' ')
        print('Por favor, digite uma das opções oferecidas')
        print(' ')
        continue
    elif iniciar == '0':
        print('Você saiu')
        break
    else:
        cpf = ''

        for n in range(9):
            cpf += str(random.randint(0,9))

        resto = primeiro_dig(cpf)
        digito1 = str(resto if resto <= 9 else 0)

        cpf += digito1
        resto2 = segundo_dig(cpf)
        digito2 = str(resto2 if resto2 <= 9 else 0)

        print(' ')
        print(f'O CPF gerado é: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{digito1+digito2}')
        print(' ')
