def rot13(palabra):
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    listaP = list(palabra)
    lenP = len(palabra)
    contador = -1
    contador2 = 0
    palabraN = ""
    for a in range(lenP):
        contador2 = 0
        contador += 1
        while True:
            if listaP[contador] == " ":
                    palabraN += " "
                    break
            elif listaP[contador] == abc[contador2]:
                if contador2 + 13 > 25:
                    contador2 -= 13
                    palabraN += abc[contador2]
                    break
                elif contador2 + 13 <= 25:
                    contador2 += 13
                    palabraN += abc[contador2]
                    break
            else:
                contador2 += 1
    return palabraN
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)