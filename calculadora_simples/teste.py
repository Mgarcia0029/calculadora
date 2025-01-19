# Início do programa
print("Bem-vindo à calculadora simples!")

# Receber os dois números para a operação
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

while True:
    # Mostrar as opções para o usuário
    print("\nEscolha uma operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Sair")

    # Receber a escolha do usuário
    opcao = input("Digite o número da operação desejada: ")

    if opcao == "1":
        resultado_soma = num1 + num2
        print(resultado_soma)
        break
    elif opcao == "2":
        resultado_subtracao = num1 - num2
        print(resultado_subtracao)
        break
    elif opcao == "3":
        resultado_multiplicacao = num1 * num2
        print(resultado_multiplicacao)
        break
    elif opcao == "4":
        resultado_divisao = num1 / num2
        print(resultado_divisao)
        break
    elif opcao == "5":
        print("Saindo do sistema. Até logo!!")      
        break  # Sai do loop
    else:
        print("Opção invalida! tente novamente.")