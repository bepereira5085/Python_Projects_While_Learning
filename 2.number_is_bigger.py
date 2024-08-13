try:
    print('')
    print("Let's discover what number is the biggest")
    print('')

    N1 = input('Type a number: ')
    N2 = input('Type another one: ')

    conv_1 = float(N1)
    conv_2 = float(N2)

    if conv_1 > conv_2:
        print(f'O primeiro número, {conv_1}, é maior que o segundo, {conv_2}')
    elif conv_2 > conv_1:
        print(f'O segundo número, {conv_2}, é maior que o primeiro, {conv_1}')
    elif conv_1 == conv_2:
        print(f'Os números são iguais, ou seja, {conv_1} = {conv_2}')

except:
    print("What you've done?, THIS IS NOT A NUMBER")