def rot13(palabra):
    palabra = list(palabra)
    alfabeto1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    alfabeto2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range (len(alfabeto1)):
        for j in range (len(palabra)):
            if palabra[j] == alfabeto1[i]:
                palabra[j] = alfabeto2[i]
            elif palabra[j] == alfabeto2[i]:
                palabra[j] = alfabeto1[i]
    palabra = "".join(palabra)
    return palabra
            
        

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
