def rot13(texto):    
    abc = "abcdefghijklmnopqrstuvwxyz"
    cifrado = ""
    for c in texto:
        if c in abc:
            cifrado += abc[(abc.index(c)+13)%(len(abc))]
        else:
            cifrado += c
    return cifrado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           