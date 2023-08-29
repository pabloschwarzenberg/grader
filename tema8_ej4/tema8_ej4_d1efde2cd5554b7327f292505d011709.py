def rot13(palabra):
    palabra = list(palabra)
    alfabeto1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    alfabeto2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for k in range(int(len(alfabeto1))):
        for i in range(len(palabra)):
            if palabra[i] == alfabeto1[k]:
                palabra[i] = alfabeto2[k]
            elif palabra[i] == alfabeto2[k]:
                palabra[i] = alfabeto1[k]
    palabra = "".join(palabra)        
    return palabra    
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)

           