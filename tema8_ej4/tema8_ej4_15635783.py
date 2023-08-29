letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
def rot13(palabra):
    rot=[]
    x=list(palabra)
    for i in x:
        rot.append(letras[letras.index(i)+13])
       
    k=("").join(rot)    
    return k

    
        
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
