class BombaCombustivel(object):
    def __init__(self, tipo_combustivel,
                 valor_litro, quantidade_combustivel):
        self._tipo_combustivel = tipo_combustivel
        self._valor_litro = valor_litro
        self._quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = float(valor)/self._valor_litro

        self._quantidade_combustivel += litros

        print "Por R$ {} é abastecido {} litros".format(valor, litros)

    def abastecer_por_litro(self, litros):
        valor = float(litros)/self._valor_litro

        self._quantidade_combustivel += litros

        print "É abastecido {} litros por R$ {}".format(litros, valor)

    def alterar_valor(self, valor):
        self._valor_litro = valor

    def alterar_combustivel(self, combustivel):
        self._tipo_combustivel = combustivel

    def alterar_quantidade_combustivel(self, quantidade_combustivel):
        self._quantidade_combustivel = quantidade_combustivel
