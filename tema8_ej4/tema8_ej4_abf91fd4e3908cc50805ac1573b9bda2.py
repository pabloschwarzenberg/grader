def rot13(palabra):

    palabra = str(palabra.lower())

    Alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    palabrarot = ""

    for i in palabra:

        A=Alfabeto.index(i)

        if Alfabeto.index(i) <= 12:

            palabrarot += Alfabeto[A+13]

        if Alfabeto.index(i) > 12:

            palabrarot += Alfabeto[A-13]

    return palabrarot

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           