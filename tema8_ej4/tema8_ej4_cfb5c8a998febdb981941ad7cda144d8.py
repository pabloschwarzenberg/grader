#Encriptador ROT13 
def rot13(palabra):
    palabra = palabra.upper()
    abc= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    abecedario= []
    for i in abc:
        abecedario.append(i)
    palabra1 = []
    for i in palabra:
        palabra1.append(i)
    i = 0
    while i< len(palabra1):
        x = abecedario.index(palabra1[i])
        if palabra1[i] < "N":
            palabra1[i] = abecedario[x+13]
        else:
            palabra1[i] = abecedario[x-13]
        i = i + 1
    palabra2 = "".join(palabra1)
    palabra2 = palabra2.lower()
    return palabra2