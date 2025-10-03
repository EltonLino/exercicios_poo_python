class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"{self.modelo} - {self.cor} ({self.ano})"
    
carro1 = Carro(modelo='Ford Mustang', cor='Vermelho', ano=2020)

print(carro1)
        