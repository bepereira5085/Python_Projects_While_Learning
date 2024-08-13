print('')
print('CALCULADORA RAPIDEX')
print('')
print('Caso deseje sair, digite "sair"')
print('')
while True:
    N1_c = input('Insira um número: ')
    if N1_c.lower() == 'sair':
        print('Você saiu')
        break
    operacao = input('Digite sua operação(+|-|*|/): ')
    if operacao.lower() == 'sair':
        print('Você saiu')
        break
    N2_c = input('Insira outro número: ')
    if N2_c.lower() == 'sair':
        print('Você saiu')
        break
    
    try:
        N1 = float(N1_c)
        N2 = float(N2_c)

        if operacao == '+':
            print(f'{N1} + {N2} = {N1 + N2: .2f}')
        elif operacao == '-':
            print(f'{N1} - {N2} = {N1 - N2: .2f}')
        elif operacao == '*':
            print(f'{N1} * {N2} = {N1 * N2: .2f}')
        elif operacao == '/':
            if N2 != 0:
                print(f'{N1} / {N2} = {N1 / N2: .2f} e o resto é {N1%N2}')
            else:
                print('Não se divide números por zero')
        else:
            print('Por favor, digite uma operação aritmética: adição, subtração, multiplicação ou divisão')
    except:
        print('Erro,insira números e operações válidos')