def rot13(palabra):
    p1="abcdefghijklm"
    p2="nopqrstuvwxyz"
    n_palabra=""
    i=0
    while i < len(palabra):
        j=0
        while j < len(p1):
            if palabra[i] == p1[j]:
                n_palabra = n_palabra + p2[j]
            elif palabra[i] == p2[j]:
                n_palabra = n_palabra + p1[j]
            j+=1
        i+=1
    return n_palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           