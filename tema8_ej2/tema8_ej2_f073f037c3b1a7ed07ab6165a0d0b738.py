def buscarTodas(a,b):
    posiciones = ""
    numero = 0
    for indice in a:
        if indice == b:
            if posiciones == "":
                numero_str = str(numero)
                posiciones += numero_str
                numero += 1
            else:
                posiciones += " "
                numero_str = str(numero)
                posiciones += numero_str
                numero += 1
        else:
            numero += 1
    return posiciones

 

if __name__ == "__main__":
    pass
           