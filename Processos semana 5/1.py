# Classe que representa um consumidor (cliente) que pode fazer compras
class Consumidor:
    def __init__(self, nome):
        self.nome = nome  # Nome do consumidor
        self.compras = []  # Lista para armazenar os pedidos realizados pelo consumidor

# Classe que representa um item (produto) disponível para compra
class Item:
    def __init__(self, caracteristicas, valor):
        self.caracteristicas = caracteristicas  # Descrição do item
        self.valor = valor  # Preço do item

# Classe que representa um pedido realizado por um consumidor
class Pedido:
    def __init__(self, consumidor, item, quantidade):
        self.consumidor = consumidor  # Consumidor que fez o pedido
        self.item = item  # Item comprado
        self.quantidade = quantidade  # Quantidade do item comprado
        self.valor_consumo = quantidade * item.valor  # Calcula o valor total do pedido
        self.status = "Compra Realizada"  # Define o status padrão do pedido
    
# Criando um consumidor chamado "Pedro Yokada"
consumidor = Consumidor("Pedro Yokada")

# Criando um item chamado "Xbox" com valor de R$5300,00
item = Item("Xbox", 5300.00)

# Criando um pedido para o consumidor, comprando 2 unidades do item
pedido = Pedido(consumidor, item, 2) 

# Adicionando o pedido à lista de compras do consumidor
consumidor.compras.append(pedido)  

# Exibindo os detalhes da compra realizada
print(f"Consumidor: {consumidor.nome}, Produto: {pedido.item.caracteristicas}, Quantidade: {pedido.quantidade}, Valor: R${pedido.valor_consumo}, Status: {pedido.status}")
