def decodificar(mensaje):
    listab = list(mensaje)
    listae = []
    final = []
    p = ''
    listab.reverse()
    conta = 0
    for i in listab:
        if i == '1':
            elevado = 2 ** conta
            conta += 1
            listae.append(elevado)
        elif i == '0':
            conta += 1
        if i == ',':
            conta = 0
            final.append(sum(listae))
            listae = []
    final.append(sum(listae))
    final.reverse()
    for i in final:
        letra = chr(i)
        p = p + letra
    return p