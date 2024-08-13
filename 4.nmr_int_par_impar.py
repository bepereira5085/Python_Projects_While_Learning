try:
    n1 = input('Digite um número inteiro: ')
    n1_int = int(n1)

    if n1_int % 2 == 0:
        print('Esse número é par')
    else:
        print('Esse número é impar')

except:
    print('Você não digitou um número inteiro')