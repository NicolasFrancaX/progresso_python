# -*- coding: utf-8 -*-

lista = [0, 0, 0, 0, 0, 0, 0]
total = 0

resposta = int(raw_input("> "))
while resposta != 0:
    lista[resposta] += 1
    resposta = int(raw_input("> "))
    total += 1

os = {
    1: "Windows Server",
    2: "Unix",
    3: "Linux",
    4: "Netware",
    5: "Mac OS",
    6: "Outro"
}

print """
Sistema Operacional     Votos   %
-------------------     -----   ----
"""

for i in range(1, 7):
    print "{}     {}   {}%".format(os[i], lista[i], (100*lista[i])/total)

print """
-------------------     -----
Total                   %5d

""" % total

os_mais_votado = os[lista.index(max(lista))]
porcentagem_mais_votado = (100*max(lista))/total

print """
O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {}% dos votos""".format(
     os_mais_votado, max(lista), porcentagem_mais_votado)

