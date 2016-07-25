# -*- coding: utf-8 -*-

import math

area_pintada = float(raw_input("Digite o tamanho (em m²) da área a ser pintada: "))

# Apenas latas
numero_latas = math.ceil(area_pintada/(18*6))
preco_latas = numero_latas*80.00

print "Latas: Quantidade: {} | Preço: {}".format(numero_latas, preco_latas)

# Apenas galoes
numero_galoes = math.ceil(area_pintada/(3.6*6))
preco_galoes = numero_galoes*25.00

print "Galões: Quantidade: {} | Preço: {}".format(numero_galoes, preco_galoes)

# Latas e galoes
numero_latas = (area_pintada - (area_pintada % (18*6)))/(18*6)
numero_galoes = math.ceil((area_pintada % (18*6))/(3.6*6))
preco_latas_com_galoes = (numero_latas*80.00) + (numero_galoes*25.00)

print "Galões: Quantidade: {} | Latas: Quantidade: {} | Preço: {}".format(numero_latas, numero_galoes, preco_latas_com_galoes)
