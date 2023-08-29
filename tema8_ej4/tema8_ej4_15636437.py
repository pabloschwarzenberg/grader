mitad1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
mitad2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]

def rot13(palabra):
    newpalabra=""
    letras=[]
    for letra in palabra:
        letras.append(letra)
    for jak in letras:
        if (jak in mitad1)==True:
            posicion=mitad1.index(jak)
            newpalabra+=mitad2[posicion]
        elif (jak in mitad2)==True:
            posicion=mitad2.index(jak)
            newpalabra+=mitad1[posicion]
    return newpalabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)