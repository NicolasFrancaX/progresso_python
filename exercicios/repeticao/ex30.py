# -*- coding: utf-8 -*-

preco_pao = float(raw_input("Preço do pão: "))

print "Panificadora Pão de Ontem - Tabela de preços"

for i in range(1, 51):
    print "%d - R$ %.2f" % (i, preco_pao*i)
