alfabeto_1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
alfabeto_2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
def rot13(palabra):
    l=len(palabra)
    palabra=list(palabra)
    for i in range(0,l):
        for k in range(0,13):
            if palabra[i]==alfabeto_1[k]:
                palabra[i]=alfabeto_2[k]
            elif palabra[i]==alfabeto_2[k]:
                palabra[i]=alfabeto_1[k]
        traducido="".join(palabra)    
    return(traducido)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           