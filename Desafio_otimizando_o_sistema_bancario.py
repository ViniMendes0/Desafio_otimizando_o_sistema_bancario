# Definir o saque

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= limite_saques:
        print("Limite diário de saques atingido.")
    elif valor > limite:
        print(f"O valor máximo para saque é de R$ {limite:.2f}.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
    return saldo, extrato, numero_saques

# Definir o Deposito

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    else:
        print("O valor do depósito deve ser positivo.")
    return saldo, extrato

# Definir o saldo


def extrato(saldo, *, extrato):
    print("\n--- Extrato ---")
    for operacao in extrato:
        print(operacao)
    print(f"Saldo atual: R$ {saldo:.2f}\n")

# Definir a criação do usuario


def criar_usuario(usuarios, nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Usuário com este CPF já existe.")
            return usuarios
    novo_usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso.")
    return usuarios

# Definir a criação da conta corrente


def criar_conta_corrente(contas, usuarios, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            nova_conta = {"agencia": "0001", "numero_conta": len(contas) + 1, "usuario": usuario}
            contas.append(nova_conta)
            print("Conta criada com sucesso.")
            return contas
    print("Usuário não encontrado.")
    return contas

# Definir a opção de excluir conta


def excluir_conta(contas,numero_conta):
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            contas.remove(conta)
            return True
        return False

# Definir a opção de exibir os dados 


def exibir_dados(usuarios, contas, cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print(f"\n--- Dados do Usuário ---")
            print(f"Nome: {usuario['nome']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Endereço: {usuario['endereco']}")
            print("\n--- Contas ---")
            for conta in contas:
                if conta['usuario']['cpf'] == cpf:
                    print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}")
            return
    print("Desculpe.Usuário não encontrado.")




# Listas para armazenar usuários e contas
usuarios = []
contas = []

# Lista para armazenar extratos
extrato_geral = []

# Menu do sistema bancário
menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar Usuário
[5] Criar Conta Corrente
[6] Excluir a conta
[7] Exibir Dados do Usuário
[0] Sair
=> """

# Variáveis iniciais
saldo = 0
limite = 500.0
numero_saques = 0
limite_saques = 3

# Loop principal
while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito por gentileza: R$ "))
        saldo, extrato_geral = depositar(saldo, valor, extrato_geral)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque por gentileza: R$ "))
        saldo, extrato_geral, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato_geral, limite=limite, numero_saques=numero_saques, limite_saques=limite_saques)
    elif opcao == "3":
        extrato(saldo, extrato=extrato_geral)
    elif opcao == "4":
        nome = input("Informe o nome: ")
        data_nascimento = input("Informe a sua data de nascimento (dd/mm/aaaa): ")
        cpf = input("Informe o seu CPF (apenas números): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        usuarios = criar_usuario(usuarios, nome, data_nascimento, cpf, endereco)
    elif opcao == "5":
        cpf = input("Informe o CPF do usuário: ")
        contas = criar_conta_corrente(contas, usuarios, cpf)
    elif opcao == "6":
        numero_conta = int(input("Por favor, informe o número da conta a ser excluida"))
        if excluir_conta(contas, numero_conta):
            print("Conta excluida com sucesso.")
        else:
            print("Conta não encontrada.")

    elif opcao == "7":
        cpf = input("Informe o CPF do usuário: ")
        exibir_dados(usuarios, contas, cpf)

    elif opcao == "0":
        print("Obrigado por usar o nosso sistema bancário!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



