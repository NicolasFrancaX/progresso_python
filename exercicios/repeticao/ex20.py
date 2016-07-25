
def fatorial(n):
    if n == 0:
        return 1
    fat = 1
    for i in range(1, n + 1):
        fat *= i

    return fat


# Condicao de parada - n ser maior ou igual a 0 e menor que 16
n = int(raw_input("> "))
while(n >= 0 and n < 16):
    print fatorial(n)

    n = int(raw_input("> "))

