#Crux Sacra Sit Mihi Lux

import random
import time

def menu():

    print("-----------38 Roulette-----------")
    print("")
    print("1 - Jogar")
    print("2 - Ver pontuação")
    print("3 - Sair")
    print("")
    print("---------------------------------")
    print("")


    try:
        
        opcao = int(input("Escolha uma opcão: "))

    except ValueError:

        print("Opção inválida, tente novamente")

    else:

        if opcao < 1 or opcao > 3:

            print("Opção inválida, tente novamente")

        else:

            return opcao

def menu_mod():

    print("")
    print("---------------------------------")
    print("")
    print("1 - Modo Normal (1 bala na câmara)")
    print("2 - Modo Insano (Quantidade aleatória de balas na câmara)")
    print("")
    print("---------------------------------")
    print("")

    try:
        
        opcao_mod = int(input("Escolha um modo: "))

    except ValueError:

        print("Modo inválido, tente novamente")

    else:

        if opcao_mod < 1 or opcao_mod > 2:

            print("Modo inválido, tente novamente")

        else:

            return opcao_mod

def carregar_revolver (opc_mod):

    if opc_mod == 1:

        revolver = [0] * 6
        carregar_bala = random.randint (0, 5)
        revolver[carregar_bala] = 1
        
        print("")
        print("Carregando a arma...")
        time.sleep (2)
        print("")
        print("Roleta preparada")
        
        return revolver
    
    elif opc_mod == 2:

        quant_balas = random.randint (1, 5)
        revolver = [0] * 6

        for i in range (quant_balas):

            carregar_bala = random.randint (0, 5)

            while revolver[carregar_bala] == 1:
                
                carregar_bala = random.randint (0, 5)

            revolver[carregar_bala] = 1
            
        print("")
        print("Carregando a arma...")
        time.sleep (2)
        print("")
        print("Roleta preparada")

        return revolver

def gameplay_loop (revolver):

    while True:

        print("")
        print("---------------------------------")
        print("")
        print("Escolha seu destino: ")
        print("")
        print("1 - Atirar em si mesmo")
        print("2 - Atirar no dealer")
        print("")
        print("---------------------------------")
        print("")

        try:

            escolha = int(input("Faça sua escolha: "))

        except ValueError:

            print("Escolha inválida, tente novamente")

        else:

            if escolha == 1:

                if revolver.pop(0) == 1:

                    time.sleep(2)
                    print("")
                    print("BANG!............")
                    print("Você perdeu")
                    print("")
                    return revolver, True, "dealer"
                
                else:

                    time.sleep(2)
                    print("")
                    print("Click......")
                    print("")
                    print("Seguro, por enquanto. Escolha novamente")

            elif escolha == 2:

                if revolver.pop(0) == 1:

                    time.sleep(2)
                    print("")
                    print("BANG!.........THUM!...")
                    print("Você venceu")
                    print("")
                    return revolver, True, "player"
                
                else:

                    time.sleep(2)
                    print("")
                    print("Click......")
                    print("")
                    print("Hora do dealer escolher")
                    return revolver, False, None

            if escolha < 1 or escolha > 2:

                print("Escolha inválida, tente novamente")

def cpu_loop(revolver):

    while True:

        print("")
        print("---------------------------------")
        print("")
        print("Escolha do Dealer: ")
        print("")
        print("1 - Atirar nele mesmo")
        print("2 - Atirar em você")
        print("")
        print("---------------------------------")
        print("")

        escolha_dealer = random.choice ([1, 2])

        if escolha_dealer == 1:

            time.sleep(2)
            print("")
            print("1 - Atirar nele mesmo")
            print("")

            if revolver.pop(0) == 1:

                time.sleep(2)
                print("")
                print("BANG!............THUM!........")
                print("Você venceu")
                print("")
                return revolver, True, "player"
                
            else:

                time.sleep(2)
                print("")
                print("Click......")
                print("")
                print("Seguro. Ele vai escolher novamente")

        elif escolha_dealer == 2:

            time.sleep(2)
            print("")
            print("2 - Atirar em você")
            print("")

            if revolver.pop(0) == 1:

                time.sleep(2)
                print("")
                print("BANG!............")
                print("Você perdeu")
                print("")
                return revolver, True, "dealer"
                
            else:

                time.sleep(2)
                print("")
                print("Click......")
                print("")
                print("Sua vez de novo")
                return revolver, False, None

def main():

    opc = 0
    placar_player = 0
    placar_cpu = 0

    while opc != 3:

        opc = menu()
        game_over = False

        if opc == 1:

            opc_mod = menu_mod()
            revolver = carregar_revolver(opc_mod)

            while game_over is False:
                
                revolver, game_over, vencedor = gameplay_loop(revolver)

                if game_over is False:
                    
                    revolver, game_over, vencedor = cpu_loop(revolver)

            if game_over is True:

                if vencedor == "player":

                    placar_player += 1

                elif vencedor == "dealer":

                    placar_cpu += 1

        elif opc == 2:
            
            print("")
            print("Vitórias do Player: ", placar_player)
            print("Vitórias da CPU: ", placar_cpu)
            print("")

main()
