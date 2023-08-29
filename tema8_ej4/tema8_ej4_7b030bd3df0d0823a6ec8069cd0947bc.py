def rot13(palabra):
    lista1 = list(palabra)#["h","o","l","a"]
    lista2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lista3 = ["n","o","p","q","r","s","t","u","v","w","x","y","z",
    "a","b","c","d","e","f","g","h","i","j","k","l","m"]
    lista4 = []
    for i in range(len(lista1)):
        if(lista1[i] != lista2[i]):
            for j in range(len(lista2)):
                if(lista1[i] == lista2[j]):
                    lista4.append(lista3[j])
    resultado = "".join(lista4)
    print(resultado)
    return resultado
    
                    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           