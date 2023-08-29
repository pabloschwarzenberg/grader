def rot13(texto):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            cifrada = alfabeto[(indice+13) % len(alfabeto)]
            #print(cifrada)
            cifrado += cifrada
        else:
            cifrado += letra
    return cifrado
 
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print(f"Palabra decodificada: {resultado}")
           
