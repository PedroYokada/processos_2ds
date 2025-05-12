class Usuario:
    def _init_(self, nome, senha):
        self.__nome = nome
        self.__senha = senha

# Uso da classe
usuario = Usuario("joao123", "senha123")
usuario.alterar_senha("novaSenha123")