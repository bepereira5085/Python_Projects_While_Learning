import random 

try:
    
    #ENTRAR OU SAIR

    while True:

        print('VAMOS BRINCAR DE FORCA??')
        entrar = input('Sim ou não?: ').lower()

        if entrar == 'sim' or entrar == 's' or entrar == 'si ':
            
            # O JOGO COMEÇA
        
            possibilidades = 'bicicleta', 'joaquim', 'pizza', 'violao', 'jogador'\
                            'fernando', 'pastel', 'ciclismo', 'gabriela', 'sorvete'\
                            'camiseta', 'rodrigo', 'macarrao', 'corrida', 'renata'\
                            'guitarra', 'alexandre', 'sanduiche', 'natalia', 'carro'\
                            'cavalo', 'luiz', 'hamburguer', 'natacao', 'carolina'\
                            'camisa', 'rafael', 'churrasco', 'skate', 'mariana'\
                            'bola', 'pedro', 'sobremesa', 'tenis', 'daniel'\
                            'futebol', 'alessandro', 'lasanha', 'basquete', 'juliana'\
                            'gol', 'ricardo', 'sopa', 'surf', 'eduarda'\
                            'mochila', 'vinicius', 'caldo', 'karate', 'julia' 
            n = random.randint(0, len(possibilidades) - 1)
            palavra = possibilidades[n] #ESCOLHE A PALAVRA
            letras_salvas = ''
            letras_dig = ''
            tentativas = 0

            while True:
                print(' ')
                letra = input('Digite uma letra: ')
                palavra_form = ''
                letras_salvas += (' ' + letra.upper()) 

                if letra in palavra:
                    letras_dig += letra
                else:
                    tentativas += 1

                for letra_secreta in palavra:
                    if letra_secreta in letras_dig:
                        palavra_form += letra_secreta
                    else: 
                        palavra_form +='*'

                print(f'Letras digitadas: {letras_salvas}')
                print(palavra_form)
                print(f'Tentativas: {tentativas}')
                

                if palavra_form == palavra:
                    print('Parabéns, você acertou!')
                    play_again = input('Deseja jogar novamente? ').lower()
                    if play_again =='sim' or play_again == 's' or play_again == 'si ':
                        continue
                    else:
                        break

                if  tentativas == 10:
                    print('Suas tentativas acabaram')
                    play_again = input('Deseja jogar novamente? ').lower()
                    if play_again == 'não' or play_again == 'nao' or play_again == 'n':
                        break
                    else:
                        continue
            
        elif entrar == 'não' or entrar == 'nao' or entrar == 'n':
            break

        else:
            print('Por favor, digite sim ou nao')
            continue
        break

    print('Você saiu, até mais')

except Exception as error:
    print(error)
