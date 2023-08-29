def rot13(palabra):
    a = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    b = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    c = list(palabra)
    for m,n in enumerate(palabra):
        for z in range(len(a)):
            if n == a[z]:
                c[m] = b[z]
            elif n == b[z]:
                c[m] = a[z]
    palabra = "".join(c)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           