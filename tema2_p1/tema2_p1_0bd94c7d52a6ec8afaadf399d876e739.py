# por favor escribe aquí tu función
def es_primo(numero):
    y = 2
    z = 3
    a = 5
    b = 7
    c = 11
    valor = ""
    if numero % y == 0:
        if numero / y != 1:
            valor = "False"
        else:
            valor = "True"
    elif numero == 1:
        valor = "False"
        
    elif numero % c == 0:
        if numero / c != 1:
            valor = "False"
        else:
            valor = "True"

    elif numero % z == 0:
        if numero / z != 1:
            valor = "False"
        else:
            valor = "True"

    elif numero % a == 0:
        if numero / a != 1:
            valor = "False"
        else:
            valor = "True"

    elif numero % b == 0:
        if numero / b != 1:
            valor = "False"
        else:
            valor = "True"
    return valor
es_primo(2)          