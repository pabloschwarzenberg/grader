def rot13(palabra):
    lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    letras=int(len(palabra))
    lista2=[]
    for letra in range(0,letras):
        letra=palabra[letra]
        lugar=int(lista.index(letra))
        cambio=lista[lugar+13]
        lista2.append(cambio)
    palabra="".join(lista2)
    return palabra
        
print(rot13("hola"))
      
      


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           