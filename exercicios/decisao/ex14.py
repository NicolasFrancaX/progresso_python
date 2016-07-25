# -*- coding: utf-8 -*-

nota_1 = float(raw_input("Digite a 1º nota:"))
nota_2 = float(raw_input("Digite a 2º nota:"))

media = (nota_1 + nota_2)/2

if media < 4:
    conceito = 'E'
    status = "Reprovado"
elif media < 6:
    conceito = 'D'
    status = "Reprovado"
elif media < 7.5:
    conceito = 'C'
    status = "Aprovado"
elif media < 9:
    conceito = 'B'
    status = "Aprovado"
elif media <= 10:
    conceito = 'A'
    status = "Aprovado"

print """
1º nota: {}
2º nota: {}
media: {}
conceito: {}
status: {}
""".format(nota_1, nota_2, media,
           conceito, status)

