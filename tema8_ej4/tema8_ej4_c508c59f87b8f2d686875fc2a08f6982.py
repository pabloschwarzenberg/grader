def rot13(palabra):
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    largo=len(palabra)
    palabra=list(palabra)
    _=0
    while _<len(palabra):
        letra=palabra[_]
        indice=abecedario.index(letra)
        indice=int(indice)
        if indice<=12:
            indice_nuevo=indice+13
            cambio = abecedario[indice_nuevo]
            palabra[_] = cambio
        if indice>12:
            indice_nuevo=indice-13
            cambio = abecedario[indice_nuevo]
            palabra[_] = cambio
        _+=1
    palabra="".join(palabra)
    return palabra
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           