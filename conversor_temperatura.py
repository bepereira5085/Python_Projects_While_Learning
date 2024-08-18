try:
    medida = input('Sua medida está em [C]elsius ou [F]ahrenheit?: ')
    medida = medida.upper()

    if 'F' not in medida and 'C' not in medida:
        print('Por favor, digite apenas F ou C, de acordo com sua medida')
    else:
        temp = input('Digite sua temperatura: ')
        
        if medida == 'F':
            temp_f = float(temp)
            calculo = ((temp_f - 32) * 5) / 9

            print(f'Sua temperatura é de {calculo: .2f}°C')
        else:
            temp_c = float(temp)
            calculo = (temp_c * 9 / 5) + 32
            
            print(f'Sua temperatura é de {calculo: .2f}°F')
    
except Exception as error:
    print(error)
