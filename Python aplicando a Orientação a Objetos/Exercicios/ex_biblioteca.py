#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from ex_import import Livro

livro1 = Livro('Pé De Pano', 'Pica pau', 1978)
livro2 = Livro('Pé De Ferro', 'Pau pica', 1987)

livro1.emprestar()

print(livro1._disponivel)
print(livro2._disponivel)

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

livro1 = Livro('Pé De Pano', 'Pica pau', 1978)
livro2 = Livro('Pé De Ferro', 'Pau pica', 1987)
livro3 = Livro("Outro Livro", "Autor", 1978)

livros = Livro.verificar_disponibilidade(1978)

for livro in livros:
    print(livro)

