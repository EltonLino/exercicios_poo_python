class Restaurante:
    def __init__(self, nome, categoria, cidade, estado, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f'Nome: {self.nome}\nCategoria: {self.categoria}\nCidade: {self.cidade}\nEstado: {self.estado}\nAtivado: {self.ativo}'
        

restaurante1 = Restaurante(nome='Serranos', categoria='Brasileira', cidade='São José dos Campos', estado='São Paulo',ativo=True)
print(restaurante1)