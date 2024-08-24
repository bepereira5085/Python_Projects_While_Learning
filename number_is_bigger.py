try:
    print('')
    print("Let's discover what number is the biggest")
    print('')

    N1 = input('Type a number: ')
    N2 = input('Type another one: ')

    conv_1 = float(N1)
    conv_2 = float(N2)

    if conv_1 > conv_2:
        print(f'The first number, {conv_1}, is bigger than the second one, {conv_2}')
    elif conv_2 > conv_1:
        print(f'The second number, {conv_2}, is bigger than the first one, {conv_1}')
    elif conv_1 == conv_2:
        print(f'The numbers are equal, so {conv_1} = {conv_2}')

except Exception as error_type:
    print("What you've done?, one of them IS NOT A NUMBER")
    print(error_type)
