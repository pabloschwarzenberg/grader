def rot13(palabra):
    Rot=[["a","n"],["b","o"],["c","p"],["d","q"],["e","r"],["f","s"],["g","t"],["h","u"],["i","v"],["j","w"],["k","x"],["l","y"],["m","z"]]
    pala = ""
    for i in palabra:
      
        for x in range(len(Rot)):
            if i in Rot[x]:
               
                if i == Rot[x][0]:
                    pala = pala + Rot[x][1]
                elif i == Rot[x][1]:
                    pala = pala + Rot[x][0]
                else:
                    pala = pala + i

    return pala 

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           