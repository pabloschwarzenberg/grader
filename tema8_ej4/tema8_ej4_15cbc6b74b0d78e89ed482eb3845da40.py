def rot13(pa):
    linea = "abcdefghijklm"
    linea1 = "nopqrstuvwxyz"
    tr = ""
    for i in pa:
        if i in linea:
           p = linea.index(i)
           tr += linea1[p]
        else:
            p = linea1.index(i)
            tr += linea[p]
    pass
    return tr
if __name__=="main_":
    pa=input("Ingresa la palabra que quieras encriptar: ")
    pa.lower()
    r=rot13(pa)
    print("El resultado es: ",r)