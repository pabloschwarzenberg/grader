letras1="ABCDEFGHIJKLMabcdefghijklm"
letras2="NOPQRSTUVWXYZnopqrstuvwxyz"
l1=list(letras1)
l2=list(letras2)
def rot13(palabra):
    po=""
    for n in palabra:
            if n in letras1:
                i = l1.index(n)
                po= po + letras2[i]
            if n in letras2:
                i= l2.index(n)
                po= po+letras1[i]
            
    return po

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           