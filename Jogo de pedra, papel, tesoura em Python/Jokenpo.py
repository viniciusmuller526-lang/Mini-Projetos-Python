#Crux Sacra Sit Mihi Lux

#Algoritmo jogo pedra papel tesoura

import random

player_count = 0
cpu_count = 0

opcao = 0


while opcao != 3:

    print("---JOGO DE PEDRA PAPEL TESOURA---")
    print("")
    print("1 - Jogar")
    print("2 - Ver pontuação")
    print("3 - Sair")
    print("")
    
    opcao = int(input("Escolha uma ação: "))

    if opcao == 1:
        
        pedra = "1"
        papel = "2"
        tesoura = "3"
        
        print("")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoura")
        print("")
        player_choice = input("Escolha uma jogada: ")
        opcoes = [pedra, papel, tesoura]
        cpu_choice = random.choice (opcoes)

        if player_choice == cpu_choice:
            
            print("")
            print("Sua escolha: ", player_choice)
            print("Escolha da CPU: ", cpu_choice)
            print("Empate")
            print("")

        if player_choice == pedra and cpu_choice == papel:

            cpu_count += 1
            print("")
            print("Sua escolha: ", player_choice)
            print("Escolha da CPU: ", cpu_choice)
            print("Perdeu")
            print("")

        elif player_choice == papel and cpu_choice == pedra:

            player_count += 1
            print("")
            print("Sua escolha: ", player_choice)
            print("Escolha da CPU: ", cpu_choice)
            print("Venceu")
            print("")

        if player_choice == papel and cpu_choice == tesoura:

            cpu_count += 1
            print("")
            print("Sua escolha: ", player_choice)
            print("Escolha da CPU: ", cpu_choice)
            print("Perdeu")
            print("")

        elif player_choice == tesoura and cpu_choice == papel:

            player_count += 1
            print("")
            print("Sua escolha: ", player_choice)
            print("Escolha da CPU: ", cpu_choice)
            print("Venceu")
            print("")

        if player_choice == tesoura and cpu_choice == pedra:

            cpu_count += 1
            print("")
            print("Sua escolha: ", player_choice)
            print("Escolha da CPU: ", cpu_choice)
            print("Perdeu")
            print("")

        elif player_choice == pedra and cpu_choice == tesoura:

            player_count += 1
            print("")
            print("Sua escolha: ", player_choice)
            print("Escolha da CPU: ", cpu_choice)
            print("Venceu")
            print("")

    elif opcao == 2:
        
        print("")
        print("Vitórias do jogador: ", player_count)
        print("Vitórias da CPU: ", cpu_count)
        print("")
