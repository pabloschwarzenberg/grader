def buscarTodas(a, b):
    localizacion = []
    cuenta = 0
    carlos = ""
    for c in a:
        if c == b:
            localizacion.append(cuenta)
        if c != "":
            cuenta += 1
    for n in localizacion:
        carlos += str(n)
        if n != 13:
            carlos += " "

    return carlos
    pass


if __name__ == "__main__":
    d = input()
    e = input()
    print(buscarTodas(d, e))
    pass
           