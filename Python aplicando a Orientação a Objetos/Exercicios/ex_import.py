# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

class Livro:
    def __init__(self, titulo, autor , ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

# Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

class Livro:
    def __init__(self, titulo, autor , ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicado}'

# livro1 = Livro('Pé De Pano', 'Pica pau', 1978)
# livro2 = Livro('Pé De Ferro', 'Pau pica', 1987)

# print(livro1)
# print(livro2)

#Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

class Livro:
    def __init__(self, titulo, autor , ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicado}'

    def emprestar(self):
        self._disponivel = False


# livro1 = Livro('Pé De Pano', 'Pica pau', 1978)
# livro2 = Livro('Pé De Ferro', 'Pau pica', 1987)

# livro1.emprestar()

# print(livro1._disponivel)
# print(livro2._disponivel)

#Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True

        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicado}'

    def emprestar(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []

        for livro in Livro.livros:
            if livro._ano_publicado == ano and livro._disponivel:
                livros_disponiveis.append(livro)

        return livros_disponiveis



# livro1 = Livro('Pé De Pano', 'Pica pau', 1978)
# livro2 = Livro('Pé De Ferro', 'Pau pica', 1987)
# livro3 = Livro("Outro Livro", "Autor", 1978)

# livros = Livro.verificar_disponibilidade(1978)

# for livro in livros:
#     print(livro)

#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.