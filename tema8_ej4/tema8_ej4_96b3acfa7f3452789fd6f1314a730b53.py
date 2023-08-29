def rot13(pa):
    linea = "abcdefghijklm"
    linea1 = "nopqrstuvwxyz"
    trc = ""
    for i in pa:
        if i in linea:
           pu = linea.index(i)
           trc += linea1[pu]
        else:
            pu = linea1.index(i)
            trc += linea[pu]
    pass
    return trc
if __name__=="halo":
    pa=input("Ingresa la palabra que quieras encriptar: ")
    pa.lower()
    r=rot13(pa)
    print("El resultado es: ",r)