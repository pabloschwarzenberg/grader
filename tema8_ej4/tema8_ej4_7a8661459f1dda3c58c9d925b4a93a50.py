def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
def rot13(palabra):

    r = list("abcdefghijklm")
    t = list("nopqrstuvwxyz")
    cifrado = ""
    for i in range(0,len(palabra)):
        if palabra[i] in r:
            cifrado += t[r.index(palabra[i])]
        else:
            cifrado += r[t.index(palabra[i])]

    return cifrado

if __name__ == "__main__":

    palabra = input('Ingrese la palabra que quieres encriptar: ')
    palabra.lower()
    resultado = rot13(palabra)
    print('El resultado es: '+resultado)
           