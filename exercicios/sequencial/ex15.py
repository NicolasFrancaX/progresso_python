# -*- coding: utf-8 -*-

def informacoes_salario(salario_bruto, ir, inss, sindicato, salario_liquido):
    impressao = """
    + Salário Bruto: R$ {}
    - IR (11%): R$ {}
    - INSS (8%): R$ {}
    - Sindicato (5%): R$ {}
    = Salário Liquido: R$ {}
    """

    return impressao.format(salario_bruto, ir,
                            inss, sindicato,
                            salario_liquido)



salario_bruto = float(raw_input("Digite seu salário: "))

inss = salario_bruto * 0.11
ir = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

desconto = inss + ir + sindicato

salario_liquido = salario_bruto - desconto

print informacoes_salario(salario_bruto, ir, inss,
                          sindicato, salario_liquido)
