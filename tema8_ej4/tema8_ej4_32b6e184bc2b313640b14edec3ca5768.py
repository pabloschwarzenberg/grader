def rot13 (mensaje):
    mensaje=mensaje.lower()
    alfabeto=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","y","z")
    texto=list(mensaje)
    nuevotexto=[]

    #CONVERTIR UN MENSAJE EN OTRO
    for letra in texto:
        letra=alfabeto.index(letra)
        letra=str(alfabeto[letra+13])
        nuevotexto.append(letra)
    nuevotexto=''.join(nuevotexto)
    texto=''.join(texto)
    return nuevotexto

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           