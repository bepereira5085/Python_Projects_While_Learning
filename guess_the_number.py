import random

print('Que tal adivinhar que número a máquina escolheu?')
print('Você tem três tentativas, o número está entre 1 e 10')

numero = random.randint(1,10)
tentativas = 0

while tentativas <= 2:
     palpite = input('Qual seu palpite?: ')
     try:
          palpite_int = int(palpite)
     except:
         print('Digite números inteiros')
         continue
     if palpite_int > 0 and palpite_int < 11:
          if palpite_int > numero:
               tentativas += 1
               print('O número é menor')
               print(f'Tentativas: {tentativas}')
          elif palpite_int < numero:
               tentativas += 1
               print('O número é maior')
               print(f'Tentativas: {tentativas}')
          else:
               tentativas += 1
               print(f'Parabéns, você acertou com {tentativas} tentativas')
               break
     else:
          print('Digite um número entre 1 e 10, amigo.')
          continue
print(f'O número é {numero}')
print('Fim de jogo!')
