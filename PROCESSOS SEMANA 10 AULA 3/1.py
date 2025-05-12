class Livro:
    def _init_(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"{livro.titulo}, {livro.autor}, {livro.ano}")

# Uso das classes
biblioteca = Biblioteca()
biblioteca.adicionar_livro(Livro("1984", "George Orwell", 1949))
biblioteca.listar_livros()