# Classe base
class Veiculo:
    def acelerar(self):
        pass

# Classe Carro
class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando.")

# Classe Motocicleta
class Motocicleta(Veiculo):
    def acelerar(self):
        print("Motocicleta acelerando.")

# Criando instâncias e chamando o método acelerar
carro = Carro()
motocicleta = Motocicleta()

carro.acelerar()          # Saída: Carro acelerando.
motocicleta.acelerar()    # Saída: Motocicleta acelerando.