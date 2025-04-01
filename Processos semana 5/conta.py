# Função para criar uma conta bancária
def cria_conta(numero, titular, saldo, limite):
    # Criamos um dicionário representando a conta com seus atributos: número, titular, saldo e limite
    conta = {"numero": numero, "titular": titular, "saldo": saldo,
             "limite": limite}
    return conta  # Retornamos a conta criada

# Função para depositar um valor na conta
def deposita(conta, valor):
    # Adicionamos o valor depositado ao saldo da conta
    conta["saldo"] += valor

# Função para sacar um valor da conta
def sacar(conta, valor):
    # Subtraímos o valor do saldo da conta
    conta["saldo"] -= valor

# Função para exibir o extrato da conta
def extrato(conta):
    # Exibimos o saldo atual da conta
    print("Saldo é {}".format(conta["saldo"]))


# Importamos as funções definidas acima a partir do módulo `conta`
from conta import cria_conta, deposita, sacar, extrato

# Criamos uma conta bancária com número 123, titular "Nico", saldo inicial de 55.0 e limite de 1000.0
conta = cria_conta(123, "Nico", 55.0, 1000.0)

# Depositamos 15.0 na conta
deposita(conta, 15.0)

# Exibimos o saldo atualizado da conta
extrato(conta)  # Deve exibir "Saldo é 70.0"

# Sacamos 20.0 da conta
sacar(conta, 20.0)

# Exibimos novamente o saldo atualizado após o saque
extrato(conta)  # Deve exibir "Saldo é 50.0"


# Adicionamos 100.0 ao saldo atual da conta
conta["saldo"] = conta["saldo"] + 100.0  

# Exibimos o saldo atualizado da conta
extrato(conta)  # Mostrará o novo saldo após o acréscimo de 100.0

# Criamos uma segunda conta bancária (conta2) manualmente como um dicionário
# Esta conta tem número 321 e saldo inicial de 200.0
conta2 = {"numero": 321, "saldo": 200.0}  

# Depositamos 200.0 na conta2 usando a função deposita
deposita(conta2, 200.0)  

# Exibimos o saldo atualizado da conta2
extrato(conta2)  # Deve exibir "Saldo é 400.0"
