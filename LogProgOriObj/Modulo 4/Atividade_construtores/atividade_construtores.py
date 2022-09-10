class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual/100))

@property
def nome(self):
    return self._nome

@nome.setter
def nome(self, valor):
    self._nome = valor

@property
def preco(self):
    return self._preco

@preco.setter
def preco(self, valor):
    if isinstance(valor, str):
        self._preco = valor

pr1 = Produto('Calça', 45)
pr1.desconto(15)
print(pr1.preco)

pr2 = Produto('Camisa', 60)
pr2.desconto(10)
print(pr2.preco)