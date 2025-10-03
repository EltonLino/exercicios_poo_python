class Pessoa:
    # O __init__ é o método construtor
    def __init__(self, nome, idade):
        # 'self' referencia o próprio objeto que está sendo criado
        self.nome = nome    # Define o atributo 'nome' do objeto
        self.idade = idade  # Define o atributo 'idade' do objeto

# Criando objetos (instâncias)
p1 = Pessoa("Carlos", 25)
p2 = Pessoa("Maria", 42)

print(p1.nome)  # Saída: Carlos
print(p2.idade) # Saída: 42

class Livro:
    # O construtor espera título e autor
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano_publicacao
        self.disponivel = True  # Atributo inicial padrão

    def info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}")

# 1. Criação do objeto - O __init__ é chamado AQUI!
livro_hp = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997)

# 2. Acessando os atributos inicializados
print(f"Livro criado: {livro_hp.titulo}")
print(f"Está disponível? {livro_hp.disponivel}")
livro_hp.info()

class Carro:
    def __init__(self, marca, modelo, ano, ligando=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

carro1 = Carro("Toyota", "Corolla", 2020)
print(f"Carro: {carro1.marca} {carro1.modelo}, Ano: {carro1.ano}")