#Crux Sacra Sit Mihi Lux

# --- CONFIGURAÇÕES GLOBAIS ---

MAX_ENERGIA = 10
MAX_FOME = 10
MIN_ENERGIA = 0
MIN_FOME = 0




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

    buff_alimentar = 2

    fome -= buff_alimentar

    if fome <= MIN_FOME:

        fome = MIN_FOME

    return fome

def brincar(energia, fome):

    custo_energia_brincar = 2

    energia -= custo_energia_brincar

    if energia <= MIN_ENERGIA:

        energia = MIN_ENERGIA

    custo_fome_brincar = 1

    fome += custo_fome_brincar

    if fome >= MAX_FOME:

        fome = MAX_FOME

    return energia, fome

def descansar(energia):

    buff_descansar = 10
    energia += buff_descansar

    if energia >= MAX_ENERGIA:

        energia = MAX_ENERGIA

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

        try:
            
            opc = menu()

        except ValueError:

            print("Opção inválida, tente novamente")

        else:

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
