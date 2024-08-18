nome = input('Insira seu nome: ')
tamanho_nome = len(nome)

nova_string = ''
n = -1

while len(nova_string) < ((tamanho_nome) * 2):
    n += 1
    nova_string += ( '*' + nome[n])

nova_string += '*'
print(nova_string)
