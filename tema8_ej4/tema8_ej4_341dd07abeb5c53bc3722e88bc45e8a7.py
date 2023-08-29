def rot13(a):
    palabra = "abcdefghijklmnopqrstuvwxyz"
    transformar = palabra[13:]+palabra[:13]
    pa_palabra = lambda c: transformar[palabra.find(c)] if palabra.find(c)>-1 else c
    return ''.join(pa_palabra(c) for c in a ) 

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           