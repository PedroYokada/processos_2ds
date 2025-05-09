class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    def get_titular(self):
        return self.__titular

    def set_titular(self, novo_titular):
        self.__titular = novo_titular

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente.")

    def exibir_informacoes(self):
        print("\n--- Informações da Conta ---")
        print("Titular:", self.get_titular())
        print("Saldo: R$", self.get_saldo())


# Programa principal
titular = input("Digite o nome do titular: ")
saldo_inicial = float(input("Digite o saldo inicial: "))
conta = ContaBancaria(titular, saldo_inicial)

while True:
    print("\nEscolha uma opção:")
    print("1 - Exibir informações da conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Alterar titular")
    print("5 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        conta.exibir_informacoes()
    elif opcao == "2":
        valor = float(input("Digite o valor a depositar: "))
        conta.depositar(valor)
        print("Depósito realizado.")
    elif opcao == "3":
        valor = float(input("Digite o valor a sacar: "))
        conta.sacar(valor)
    elif opcao == "4":
        novo_titular = input("Digite o novo nome do titular: ")
        conta.set_titular(novo_titular)
        print("Titular alterado com sucesso.")
    elif opcao == "5":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida.")
