def menu():
    menu = """
    O que deseja?
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Novo cliente
    [mc] Mostrar clientes
    [cc] Criar conta
    [ec] Exibir contas
    [q] Sair

    => """
    return input(menu)

def menu_secundario():
    menu_secundario = """
    Deseja realizar mais alguma operação?

    [y]Sim
    [q]Não

    => """
    return input(menu_secundario)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito efetuado com sucesso.")
    else:
        print("Depósito não efetuado! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saldo:
        print("Saque não efetuado! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Saque não efetuado! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Saque não efetuado! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso! Retire o dinheiro.")
    else:
        print("Saque não efetuado! O valor informado é inválido.")
    return saldo, extrato, numero_saques
    
def consulta_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def novo_cliente(clientes):
    cpf = input("Digite um CPF: ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("\nCliente já existente!")
            return
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite a sua data de nascimento: ")
    endereco =  input("Digite seu endereço (logradouro, nro - bairro - cidade/UF): ")
    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\nNovo cliente cadastrado com sucesso!")

def mostrar_clientes(clientes):
    for cliente in clientes:
        print(f"""              
            Cliente: {cliente["nome"]}
            Data de nascimento: {cliente["data_nascimento"]}
            CPF: {cliente["cpf"]}
            Endereço: {cliente["endereco"]}""")

def nova_conta(agencia, conta, contas, clientes):

    cpf = input("Digite um CPF: ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            conta += 1
            contas.append({"cliente": cliente["nome"], "agencia": agencia, "conta": conta})
            print("\nConta criada com sucesso!")
            return conta    
    print("\nCliente não cadastrado, realize o cadastro antes de criar a conta.")

def exibir_contas(contas):
    for conta in contas:
        print(f"""              
              Titular: {conta["cliente"]}
              Agência: {conta["agencia"]}
              Conta: {conta["conta"]}""")

def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    clientes = []
    contas = []
    AGENCIA = "0001"
    conta = 0

    print("Bom dia, bem vindo ao nosso auto-atendimento.")
    opcao = menu()

    while True:    

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)        

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

        elif opcao == "e":
            consulta_extrato(saldo, extrato=extrato)
        
        elif opcao == "nc":
            novo_cliente(clientes)

        elif opcao == "mc":
            mostrar_clientes(clientes)

        elif opcao == "cc":
            conta = nova_conta(AGENCIA, conta, contas, clientes)

        elif opcao == "ec":
            exibir_contas(contas)

        elif opcao == "y":
            opcao = menu()
            continue

        elif opcao == "q":
            print("\nAgradecemos sua visita, tenha um bom dia!")
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            opcao = menu()
            continue

        opcao = menu_secundario()

main()