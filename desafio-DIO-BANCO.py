# Sistema Bancário Simples - Projeto DIO (Versão personalizada)

LIMITE_SAQUE_DIARIO = 3
VALOR_LIMITE_SAQUE = 500.00

saldo = 0.0
extrato = []
saques_realizados = 0

menu = """
╔════════════════════════╗
║       MENU BANCÁRIO    ║
╠════════════════════════╣
║ [d] Depositar          ║
║ [s] Sacar              ║
║ [e] Extrato            ║
║ [q] Sair               ║
╚════════════════════════╝
=> """

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Operação falhou: valor inválido para depósito.")

    elif opcao == "s":
        if saques_realizados >= LIMITE_SAQUE_DIARIO:
            print("Limite diário de saques atingido.")
            continue

        valor = float(input("Informe o valor do saque: R$ "))

        if valor <= 0:
            print("Operação falhou: valor inválido para saque.")
        elif valor > saldo:
            print("Saldo insuficiente para saque.")
        elif valor > VALOR_LIMITE_SAQUE:
            print(f"O valor máximo permitido por saque é R$ {VALOR_LIMITE_SAQUE:.2f}.")
        else:
            saldo -= valor
            saques_realizados += 1
            extrato.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "e":
        print("\n Extrato Bancário")
        print("-" * 30)
        if extrato:
            for movimento in extrato:
                print(movimento)
        else:
            print("Nenhuma movimentação registrada.")
        print("-" * 30)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("-" * 30)

    elif opcao == "q":
        print("Sessão encerrada. Obrigado por utilizar nosso sistema!")
        break

    else:
        print("⚠️ Opção inválida. Por favor, escolha uma opção do menu.")
