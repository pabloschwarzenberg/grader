import string
def rot13(palabra):
    #palabra = input("Ingresa la palabra que quieras encriptar: ")
    #palabra.lower()
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

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           