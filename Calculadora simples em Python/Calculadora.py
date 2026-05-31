#Crux Sacra Sit Mihi Lux

def menu():

    print("")
    print("--- CALCULADORA ---")
    print("")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print("")
    
    opcao = int(input("Escolha uma ação: "))

    return opcao

def soma(valor1, valor2):

    resultado = valor1 + valor2
    return resultado

def subtracao(valor1, valor2):

    resultado = valor1 - valor2
    return resultado

def multiplicacao(valor1, valor2):

    resultado = valor1 * valor2
    return resultado

def divisao(valor1, valor2):

    if valor2 == 0:

        print("Hoje não espertinho ;)")

    else:
        
        resultado = valor1 / valor2
        return resultado


def main():

    opc = 0

    while opc != 5:
        
        opc = menu()

        if opc == 1:

            valor1 = float(input("Insira um valor: "))
            valor2 = float(input("Insira mais um valor: "))
            resultado = soma(valor1, valor2)
            print("Seu resultado é: ", resultado)
            
        elif opc == 2:

            valor1 = float(input("Insira um valor: "))
            valor2 = float(input("Insira mais um valor: "))
            resultado = subtracao(valor1, valor2)
            print("Seu resultado é: ", resultado)
        
        elif opc == 3:

            valor1 = float(input("Insira um valor: "))
            valor2 = float(input("Insira mais um valor: "))
            resultado = multiplicacao(valor1, valor2)
            print("Seu resultado é: ", resultado)

        elif opc == 4:

            valor1 = float(input("Insira um valor: "))
            valor2 = float(input("Insira mais um valor: "))
            resultado = divisao(valor1, valor2)
            print("Seu resultado é: ", resultado)

        elif opc > 5 or opc < 1:

            print("Opção inválida, tente novamente")

main()
