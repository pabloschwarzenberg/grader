abc = "abcdefghijqlmnñopqrstuvwxyz"
def encriptar(palabra):
    encriptado = ""
    for i in range(len(palabra)):
        if palabra[i] == "z":
            encriptado = encriptado + "a"
        else:
            encriptado = encriptado + (abc[abc.index(palabra[i])+1])
    return encriptado

