#Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'O individuo {self.nome} tem {self.idade} anos de idade e trabalha com {self.profissao}'

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f'Olá, {self.nome}! Você trabalha com {self.profissao}.'


#Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

# a classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'O Sr.{self.titular} esta com R${self.saldo:.2f} de saldo!'

conta_1 = Conta_Bancaria('lucca', 500000)
conta_2 = Conta_Bancaria('João', 1000)

print(conta_1.titular)
print(conta_1.saldo)

# Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

class Conta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        return f'O Sr.{self.titular} esta com R${self.saldo:.2f} de saldo!'

    @property
    def ativa_conta(self):
        return 'Conta ativa' if self.ativo else 'Conta Desativada'

    def alternar_estado(self):
        self.ativo = not self.ativo


conta_1 = Conta_Bancaria('lucca', 500000)
conta_2 = Conta_Bancaria('João', 1000)
conta_1.alternar_estado()


print(conta_1)
print(conta_2)