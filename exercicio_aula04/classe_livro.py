class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True


    def descricao_do_livro(self):
        return f"Informações do Livro\nTítulo: {self._titulo}\nAutor: {self._autor}\nAno de publicação: {self._ano_publicacao}"

    