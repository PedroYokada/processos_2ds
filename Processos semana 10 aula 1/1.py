class Lampada:
    def __init__(self):
        self.status = False  # Começa desligada

    def ligar(self):
        self.status = True

    def desligar(self):
        self.status = False

    def mostrar_status(self):
        return "Ligada" if self.status else "Desligada"


while True:
    lampada = Lampada()

    comando = input("Digite 'l' para ligar ou 'd' para desligar ou 's' para sair: ").lower()

    if comando == 'l':
        lampada.ligar()
    elif comando == 'd':
        lampada.desligar()
    elif comando == 's':
        break
    else:
        print("Comando inválido.")
        continue  # Volta para o início do loop

    print("Estado da lâmpada:", lampada.mostrar_status())
