menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float (input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Insira um valor válido!")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Insira o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_limite_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_limite:
            print("Operação falhou, o valor de saque é maior que o limite ")

        elif excedeu_saldo:
            print("Operação falhou, valor de saque maior que o saldo da conta. ")

        elif excedeu_limite_saques:
            print("Operação falhou, você atingiu o limite de saques diários. ")

        elif valor > 0:
            saldo -= valor
            extrato += f" Saque: R$ {valor: .2f}\n"
            numero_saques += 1
    
        else :
            print("Operação falhou, o valor informado é inválido.")

    elif opcao == "e":
        print("Extrato")
        print("\n======================EXTRATO======================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==============================================")

    elif opcao == "q":
        print("Sair")
        break

    else:
        print("Operação Inválida, por favor, selecione novamente uma opção válida.")
