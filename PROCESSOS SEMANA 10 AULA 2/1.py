class ContaBancaria:
    def _init_(self, titular, saldo):
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


# Programa principal
titular = input("Digite o nome do titular: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

conta = ContaBancaria(titular, saldo_inicial)

