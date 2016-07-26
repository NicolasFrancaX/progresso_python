# -*- coding: utf-8 -*-

print """
Projeção de Gastos com Abono
============================
"""

salarios = []
abonos = []

salario = float(raw_input("Salário: "))
while salario != 0:
    salarios.append(salario)
    salario = float(raw_input("Salário: "))

total_abonos = 0
numero_valor_minimo = 0

print "Salário           - Abono"
for salario in salarios:
    abono = salario * 0.2

    if abono <= 100:
        abono = 100
        numero_valor_minimo += 1

    print "R$ {} - R$ {}".format(salario, abono)

    abonos.append(abono)
    total_abonos += abono

print """
Foram processados {} colaboradores
Total gasto com abonos: R$ {}
Valor mínimo pago a {} colaboradores
Maior valor de abono pago: R$ {}
""".format(len(abonos), total_abonos, numero_valor_minimo,
           max(abonos))
