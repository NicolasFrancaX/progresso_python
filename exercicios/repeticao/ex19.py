# -*- coding: utf-8 -*-

# Fazendo como funcao pra facilitar a vida. :)
def programa(lista):
    for x in lista:
        if x < 0 or x > 1000:
            lista.remove(x)


    print "O menor número da lista é: {}".format(min(lista))
    print "O maior número da lista é: {}".format(max(lista))

    sum = 0

    for x in lista:
        sum += x

    print "A soma dos elementos da lista é: {}".format(sum)


