class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def envelhecer(self, anos):
        self._idade += anos

        i = 0
        while i < anos and self._idade < 21:
            self._altura += 0.5

    def engordar(self, massa):
        self._peso += massa

    def emagrecer(self, massa):
        self._peso -= massa

    def crescer(self, altura):
        self._altura += altura

