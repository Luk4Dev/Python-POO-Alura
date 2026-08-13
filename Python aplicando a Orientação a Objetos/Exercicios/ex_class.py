# Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.
# Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):
# nome
# artista
# duracao
# Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..



class musica():

    nome = ''
    artista = ''
    duracacao = int

    pass

musica1 = musica()
musica1.nome = 'Bohemian Rhapsody'
musica1.artista = 'Queen'
musica1.duracao = 355

musica2 = musica()
musica2.nome = 'Imagine'
musica2.artista = 'John Lennon'
musica2.duracao = 183

musica3 = musica()
musica3.nome = 'Shape of You'
musica3.artista = 'Ed Sheeran'
musica3.duracao = 234

## Exercicios (Não Obrigatorios)

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()
restaurantes = [restaurante_praca, restaurante_pizza]


# Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

restaurante_praca.categoria = 'Italiana'

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

print(f'{restaurante_praca.nome}')

if restaurante_praca.ativo == True:
    print(f'|O Restaurante:{restaurante_praca.nome}| esta atualmente ativado|')
else:
    print(f'|O Restaurante:{restaurante_praca.nome}| esta atualmente Desativado|')

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante e armazene em uma variável chamada categoria.

categoria = Restaurante.categoria

# Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistrô'

# Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria está correta!')

# Mude o estado da instância restaurante_pizza para ativo.

restaurante_pizza.ativo = True

# Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'{restaurante_praca.nome} | {restaurante_praca.categoria} | {restaurante_praca.ativo}')