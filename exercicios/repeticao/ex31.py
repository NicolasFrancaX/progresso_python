# -*- coding: utf-8 -*-

print "Lojas Tabajara"

total = 0
i = 1

produto = 1
while produto != 0:
    produto = float(raw_input("Produto %d: R$: " % i))
    total += produto
    i += 1

print "Total: R$ %.2f" % total

dinheiro = float(raw_input("Dinheiro: R$ "))
troco = dinheiro - total

print "Troco: R$ %.2f" % troco
