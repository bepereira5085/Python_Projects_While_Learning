import os

lista = []

while True:
    os.system('cls')
    print('LISTA DE COMPRAS')
    print('O que você deseja?')
    action = input('Adiconar, Consultar ou Excluir um item: ').lower()
        
    if action.startswith('a'):
        item = input('Que produto quer adicioanr à lista: ')
        os.system('cls')
        lista.append(item)
        lista_num = enumerate(lista, start = 1)
        lista_final = lista.copy()

        print('LISTA DE COMPRAS')
        for num, prod in lista_num:
            print(num, '.' ,prod)
        print(' ')
        print('Item adicionado com sucesso!')
        seguir = input('Aperte enter para continuar')
        if seguir:
            continue
    
    if action.startswith('c'):
        os.system('cls')
        if lista != []:
            lista_num = enumerate(lista, start = 1)

            print('LISTA DE COMPRAS')
            for num, prod in lista_num:
                print(num, '.' ,prod)
        else:
            print('Ainda não há itens na sua lista!')
        seguir = input('Aperte enter para continuar')
        if seguir:
            continue

    if action.startswith('e'):
        os.system('cls')
        lista_num = enumerate(lista, start = 1)

        print('LISTA DE COMPRAS')
        for num, prod in lista_num:
            print(num, '.' ,prod)

        excluir = input('Digite o número do item que deseja excluir: ')
        n = int(excluir)
        del lista[(n - 1)]
        print('Item excluído com sucesso!')
        seguir = input('Aperte enter para continuar')
        if seguir:
            continue
