try:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))

    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        print(numero1 + numero2)
    elif operacao == '-':
        print(numero1 - numero2)
    elif operacao == '*':
        print(numero1 * numero2)
    elif operacao == '/':
        if numero2 == 0:
            print("Erro: divisão por zero não é permitida")
        else:
            print(numero1 / numero2)
    else:
        print("Voce digitou uma operação inválida")
except:    print("Erro: por favor, digite um número válido")