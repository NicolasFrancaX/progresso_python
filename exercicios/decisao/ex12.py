# -*- coding: utf-8 -*-

def informacoes_salario(horas, preco_hora):
    salario_bruto = float(horas * preco_hora)
    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11

    if salario_bruto <= 900:
        porcentagem_ir = 0
    elif salario_bruto <= 1500:
        porcentagem_ir = 0.05
    elif salario_bruto <= 2500:
        porcentagem_ir = 0.1
    else:
        porcentagem_ir = 0.2

    ir = salario_bruto * porcentagem_ir

    total_descontos = ir + inss
    salario_liquido = salario_bruto - total_descontos

    return """
    Salário Bruto: ({} * {})        : R$ {}
    (-) IR ({} %)                    : R$ {}
    (-) INSS ( 10% )                : R$ {}
    FGTS (11%)                      : R$ {}
    Total de descontos              : R$ {}
    Salário Liquido                 : R$ {}
    """.format(horas, preco_hora, salario_bruto,
               porcentagem_ir * 100, ir, inss, fgts,
               total_descontos, salario_liquido)

horas_trabalhadas = float(raw_input("Digite quantas horas você trabalhou no mês:"))
preco_hora = float(raw_input("Digite o preço da sua hora:"))
print informacoes_salario(horas_trabalhadas, preco_hora)
