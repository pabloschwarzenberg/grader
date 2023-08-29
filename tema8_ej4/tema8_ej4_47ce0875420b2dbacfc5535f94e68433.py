def rot13(palabra):
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra=list(palabra)
    long_p=len(palabra)
    i=0
    for i in range(0,long_p):
        posicion=abc.index(palabra[i])
        if posicion<=13:
            palabra.pop(i)
            palabra.insert(i,abc[posicion+13])
        else:
            abc.reverse()
            palabra.pop(i)
            palabra.insert(i,abc[38-posicion])
            abc.reverse
        print(palabra)
        i=i+1
    palabra="".join(palabra)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)