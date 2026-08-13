# Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    modelo = ''
    cor = ''
    ano = 0

hyundai = Carro()
hyundai.modelo = 'Hb20'
hyundai.cor = 'vermelho'
hyundai.ano = 2005

print(hyundai.modelo, hyundai.ano, hyundai.cor)

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante:
    nome = ''
    categoria = ''
    valor = 0
    entrega = False
    ativo = False

restaurante_do_zé = Restaurante()
restaurante_do_zé.nome = 'Seu Zé'
restaurante_do_zé.categoria = 'Caseira'
restaurante_do_zé.valor = float(45.75)

# Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, valor):
        self.nome = nome
        self.categoria = categoria
        self.valor = float(valor)
        self.entrega = False
        self.ativo = False
        Restaurante.restaurantes.append(self)

restaurante_do_zé = Restaurante('Seu zé', 'Caseira', 45)

print(restaurante_do_zé.nome, restaurante_do_zé.categoria, restaurante_do_zé.valor)

# Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, valor):
        self.nome = nome
        self.categoria = categoria
        self.valor = float(valor)
        self.entrega = False
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.valor}'

restaurante_do_zé = Restaurante('Seu zé', 'Caseira', 45)

print(restaurante_do_zé)

# Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

class Client:
    def __init__(self, name, age, table_number, order):
        self.name = name
        self.age = int(age)
        self.table_number = int(table_number)
        self.order = order

    def __str__(self):
        return f'{self.name} | {self.age} | {self.Ntable} | {self.order}'

cliente1 = Client('Rogerio', 24, 8, 'lasanha')
cliente2 = Client('Maria', 31, 3, 'pizza')
cliente3 = Client('João', 19, 5, 'hamburguer')

print(cliente1,
      cliente2,
      cliente3
      )