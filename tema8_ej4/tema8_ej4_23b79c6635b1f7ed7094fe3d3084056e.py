def rot13(palabra):
    palabraminus = palabra.lower()
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    mensajecifrado = ""
    
    for i in (palabraminus):
        if i == "":
            mensajecifrado += ""
        
        elif  i != "":
            posicion = 0
        
            posicion = abecedario.index(i)
            posicionnueva = 0
            
            if (0 <= posicion <= 12):
                posicionnueva = (posicion + 13)
                
            elif (13 <= posicion <= 25):
                posicionnueva = (posicion - 13)
        
            mensajecifrado += abecedario[posicionnueva]
    
    return mensajecifrado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           