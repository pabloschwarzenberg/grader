def rot13(palabra):
    alfabeto1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    alfabeto2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra = list(palabra)
    indexada = []
    for i in palabra:
        if i in alfabeto1:
            pos1 = alfabeto1.index(i)
            indexada.append(alfabeto2[int(pos1)])

        elif i in alfabeto2:
            pos2 = alfabeto2.index(i)
            indexada.append(alfabeto1[int(pos2)])


    indexada = "".join(indexada)
    palabra = "".join(palabra)
    
    return indexada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           