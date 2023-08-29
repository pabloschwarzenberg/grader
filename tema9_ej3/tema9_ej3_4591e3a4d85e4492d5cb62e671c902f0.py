def decodificar(mensaje):
    Mensaje_dec=""
    Nros=str(mensaje).split(",")
    for nros in Nros:
        Mensaje_dec+=chr(binario(nros))
    return Mensaje_dec
def binario(bin):
    bin=str(bin)
    dec=0
    Lista_bin = list(bin)
    for nro in range(len(Lista_bin)):
        dec+=(int(Lista_bin[nro])*(2**abs(len(Lista_bin)-1-int(nro))))
    return dec