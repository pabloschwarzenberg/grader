# por favor escribe aquí tu función
def es_primo(numero):
    con = 0
    estado = False
    for i in range(1, numero + 1):
        if numero % i == 0:
            con += 1
    if con == 2:
        estado = True
    else:
        estado = False
    return estado