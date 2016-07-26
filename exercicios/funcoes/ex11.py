def verificar_data(data):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = data[6:]

    if dia < 1 or dia > 31:
        return None
    elif mes < 1 or mes > 12:
        return None
    elif len(ano) != 4:
        return None
    else:
        return True

def por_extenso(data):
    if not verificar_data(data):
        return None

    meses = {
        "01": "janeiro",
        "02": "fevereiro",
        "03": "março",
        "04": "abril",
        "05": "maio",
        "06": "junho",
        "07": "julho",
        "08": "agosto",
        "09": "setembro",
        "10": "outubro",
        "11": "novembro",
        "12": "dezembro"
    }

    dia = data[0:2]
    mes = data[3:5]
    ano = data[6:]

    return "{} de {} de {}.".format(dia, meses[mes], ano)
