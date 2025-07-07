def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [q] Sair
    => """
    return input(menu)


def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"\nSaldo: R${saldo:.2f}")
    print("==============================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero": numero_conta, "usuario": usuario}

    print("Usuário não encontrado. Conta não criada.")
    return None


# ============ Programa principal ============

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []

while True:
    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida. Selecione novamente.")
