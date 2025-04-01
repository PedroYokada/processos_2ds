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
    def __init__(self,consumidor, item, quantidade):
        self.consumidor = consumidor  # Consumidor que fez o pedido
        self.item = item  # Item comprado
        self.quantidade = quantidade  # Quantidade do item comprado
        self.valor_consumo = quantidade * item.valor  # Calcula o valor total do pedido
        self.status = "Compra Realizada"  # Define o status padrão do pedido

# Criando consumidores
consumidor = Consumidor("Sub-Zero")
consumidor2 = Consumidor("Leon Scott Kennedy")

# Criando itens
item = Item("Xbox", 5300.00)
item2 = Item("Playstation", 4300.00)

# Criando pedidos
pedido = Pedido(consumidor, item, 1)
pedido2 = Pedido(consumidor2, item2, 1)

# Adicionando os pedidos às listas de compras dos consumidores
consumidor.compras.append(pedido)
consumidor2.compras.append(pedido2)

# Exibindo os detalhes das compras realizadas
print(
    f"Consumidor: {consumidor.nome}, Produto: {pedido.item.caracteristicas}, \n"
    f"Quantidade: {pedido.quantidade}, Valor: R${pedido.valor_consumo:.2f}, \n"
    f"Status: {pedido.status}\n"
)

print(
    f"Consumidor: {consumidor2.nome}, Produto: {pedido2.item.caracteristicas}, \n"
    f"Quantidade: {pedido2.quantidade}, Valor: R${pedido2.valor_consumo:.2f}, \n"
    f"Status: {pedido2.status}"
)
