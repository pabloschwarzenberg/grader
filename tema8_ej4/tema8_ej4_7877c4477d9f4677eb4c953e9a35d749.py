def rot13(palabra):
    abc = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    rot13 = ""
    listAbc = []
    listPalabra = []
    numberAbc = len(abc)
    numberPalabra = len(palabra)
    j = 0
    i = 0
    x = 0
    while x<len(palabra):
        listPalabra.append(palabra[x])
        x = x+1  
    while j<numberAbc:
        listAbc.append(abc[j])
        j = j+1
    while i<numberPalabra:
        posicion = listAbc.index(listPalabra[i])
        letter = listAbc[posicion+13]
        rot13 = rot13+letter
        i = i+1
    return rot13
resultado = rot13("hola")

print("El resultado es: ",resultado)