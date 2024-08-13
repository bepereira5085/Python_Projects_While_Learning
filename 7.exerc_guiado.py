nome = 'Bernardo'
tamanho_nome = len(nome)

nova_string = ''
n = -1

while len(nova_string) <= 15:
    n += 1
    nova_string += ( '*' + nome[n])
    print(nova_string)

nova_string += '*'
print(nova_string)