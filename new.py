# Início do código

# Função principal
def calculadora():
    while True:
        # Solicitar entrada de dois números
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        # Mostrar opções de operação
        print("\nEscolha uma operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")

        # Solicitar a operação desejada
        operacao = input("Digite o número da operação desejada (1/2/3/4): ")

        # Realizar a operação escolhida
        if operacao == '1':
            resultado = num1 + num2
            print(f"\nResultado da adição: {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"\nResultado da subtração: {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"\nResultado da multiplicação: {resultado}")
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado da divisão: {resultado}")
            else:
                print("\nErro: Divisão por zero não é permitida.")
        else:
            print("\nOperação inválida. Tente novamente.")

        # Perguntar se o usuário deseja realizar outra operação
        continuar = input("\nDeseja realizar outra operação? (s/n): ")
        if continuar.lower() != 's':
            print("Obrigado por usar a calculadora!")
            break

# Chamada da função principal
calculadora()