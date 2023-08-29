def rot13(palabra):
    letras="abcdefghijklmnopqrstuvwxyz"
    letras2="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    p=""
    for letra in palabra:
        for l in letras:
            if l==letra:
                p=p+letras2[letras2.find(l)+13]
    return p
                
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           