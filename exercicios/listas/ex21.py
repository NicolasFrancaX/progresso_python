# -*- coding: utf-8 -*-

print "Comparativo de Consumo de Combustível"

modelos = []
gastos = []

for i in range(0, 5):
    print "Veículo {}".format(i + 1)
    modelos.append(raw_input("Nome: "))
    gastos.append(float(raw_input("Km por litro: ")))

print "Relatório Final"

for i in range(0, 5):
    litros_100_kms = 1000/gastos[i]
    preco_litros = 2.25*litros_100_kms

    print "{} - {}   - {} - {} litros - R$ {}".format(
        i + 1, modelos[i], gastos[i], litros_100_kms, preco_litros)

print "O menor consumo é do {}.".format(modelos[gastos.index(max(gastos))])
