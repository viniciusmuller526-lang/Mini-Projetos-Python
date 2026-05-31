#Crux Sacra Sit Mihi Lux

def menu():

    print("")
    print("--- Mini Tamagotchi ---")
    print("")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Descansar")
    print("4 - Ver Status")
    print("5 - Sair")
    print("")
    
    opcao = int(input("Escolha uma ação: "))

    return opcao

def alimentar (fome):

    fome -= 2

    if fome <= 0:

        fome = 0

    return fome

def brincar(energia, fome):

    energia -= 2

    if energia <= 0:

        energia = 0

    fome += 1

    if fome >= 10:

        fome = 10

    return energia, fome

def descansar(energia):

    energia += 10

    if energia >= 10:

        energia = 10

    return energia

def ver_status (energia, fome):

    print("")
    print("Energia: ", energia)
    print("Fome: ", fome)
    print("")


def main():

    opc = 0
    fome = 5
    energia = 5

    while opc != 5:

        opc = menu()

        if opc == 1:

            fome = alimentar(fome)

        elif opc == 2:

            energia, fome = brincar(energia, fome)

        elif opc == 3:

            energia = descansar(energia)

        elif opc == 4:

            ver_status(energia, fome)

        elif opc < 1 or opc > 5:

            print("Opção inválida, tente novamente")


main()
