alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def rot13(palabra):
    parola=list(palabra)
    for i in range(len(parola)):
        posab=alfabeto.index(parola[i])
        if posab+i>=13:
            parola[i]=alfabeto[posab-13]
        elif posab+i<13:
            parola[i]=alfabeto[posab+13]
    palabra="".join(parola)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           