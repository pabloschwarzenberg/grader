# por favor escribe aquí tu función
def es_primo(numero):
    conta = 1
    divi = 1
    while (divi < numero):
        if numero % divi == 0:
            conta = conta+ 1
        divi = divi + 1
    if conta == 2:
        valor = True
    elif conta != 2:
        valor = False
    return valor