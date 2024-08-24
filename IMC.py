try:

    print('Descubra seu IMC')
    
    nome = input('Seu nome: ')
    peso = float(input('Peso em kg: '))
    altura = float(input('Altura em metros: '))
    imc = peso / (altura ** 2)
    imc = float(imc) #Pra garantir né

    #TABELA

    print(f'Olá, {nome}, seu IMC é de {imc: .2f} kg/m²')

    if imc < 18.5:
        print('Sua classificação é magreza')
    elif imc < 25:
        print('Sua classificação é saudável')
    elif imc < 30:
        print('Sua classificação é sobrepeso')
    elif imc < 35:
        print('Sua classificação é obesidade grau I')
    elif imc < 40: 
        print('Sua classificação é obesidade grau II')
    else: 
        print('Sua classificação é obesidade grau III')

except Exception as error:
    print(error)
