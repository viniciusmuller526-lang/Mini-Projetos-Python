#Crux Sacra Sit Mihi Lux

def menu():

    print("")
    print("--- Gerenciador de Lista de Compras ---")
    print("")
    print("1 - Adicionar Item")
    print("2 - Remover Item")
    print("3 - Mostrar Lista Completa")
    print("4 - Sair")
    print("")
    
    opcao = int(input("Escolha uma ação: "))

    return opcao

def adc_item (lista):

    novo_item = input("Insira um item a lista de compras: ")
    lista.append(novo_item)

    return lista

def remove_item(lista):

    remover_item = input("Insira o nome do item que deseja remover: ")
    
    if remover_item in lista:
    
        lista.remove (remover_item)

    else:

        print("Este item não existe, tente novamente")

    return lista

def mostrar_lista(lista):

    for itens in lista:

        print(itens)

def main():

    opc = 0
    lista = []

    while opc != 4:

        opc = menu()

        if opc == 1:

            lista = adc_item(lista)

        elif opc == 2:

            lista = remove_item(lista)

        elif opc == 3:

            mostrar_lista(lista)

        elif opc < 1 or opc > 4:

            print("Opção inválida, tente novamente")


main()
