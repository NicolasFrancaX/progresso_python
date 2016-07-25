# -*- coding: utf-8 -*-

def primo(n):
    div = 0

    for i in range(1, n + 1):
        if n % i == 0:
            div += 1

    return div == 2

y = int(raw_input("Ele é um número primo ou não? "))
print primo(y)
