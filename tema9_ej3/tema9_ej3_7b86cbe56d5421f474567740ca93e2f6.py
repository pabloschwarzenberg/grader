def decodificar(msj):
    msj = msj.split(",")
    palabra = []
    for i in msj:
        cifrado = 0 
        exp = 7
        for k in i:
            operatoria = 2 ** exp
            if k == "0":
                cifrado += 0
            else:
                cifrado += operatoria
            exp -= 1
        letra = chr(cifrado)
        palabra.append(letra)
        msj = "".join(palabra)
    return msj

if __name__ == "_main_":
    msj=decodificar("01101000,01101111,01101100,01100001")
    print(msj)