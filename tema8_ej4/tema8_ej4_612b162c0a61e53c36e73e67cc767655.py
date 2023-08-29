def rot13(palabra):
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
    palabra=list(palabra)
    for i in range(0,len(palabra)):
        y=abecedario.index(palabra[i])
        if y<13:
            palabra[i]=abecedario[y+13]
        else:
            palabra[i]=abecedario[y-13]
    palabra="".join(palabra)    
    return (palabra)
                        

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           