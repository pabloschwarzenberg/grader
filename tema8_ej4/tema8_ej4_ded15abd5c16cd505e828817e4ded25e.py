def rot13(palabra):
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra=list(palabra)
    contador=0
    for letra in palabra:
        y=abecedario.index(letra)
        if y>12:
            palabra[contador]=abecedario[y-13]
            contador+=1
        else:
            palabra[contador]=abecedario[y+13]
            contador+=1
    palabra="".join(palabra)
    return palabra
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           