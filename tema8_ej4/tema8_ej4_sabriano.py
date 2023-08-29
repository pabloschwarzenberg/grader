def rot13(palabra):
    letras1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    letras2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in palabra:
        if i in letras1:
            a=letras1.index(i)
            palabra=palabra.replace(i,letras2[a],1)
        elif i in letras2:
            a=letras2.index(i)
            palabra=palabra.replace(i,letras1[a],1)
    return palabra
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           