palavra = input('Insira uma palavra e descubra se é um palíndromo: ')

if palavra.isalpha():
    if (palavra[::-1]) == palavra:
        print(f'{palavra} é um palíndromo')
    else:
        print(f'{palavra} não é um palíndromo')
else:
    print('Digite apenas letras e sem espaços')