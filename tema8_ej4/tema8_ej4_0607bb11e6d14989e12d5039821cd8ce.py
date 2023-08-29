def rot13(Texto):
    Encriptado=list(Texto)
    Encriptado2=list(Texto)
    letras=  ("abcdefghijklmnopqrstuvwxyz")
    letras13=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    c=0
    d=0
    
    for p in letras:
        if p in Encriptado2 and Texto.find(p)!=-1:
         while p in Encriptado2:
           Encriptado[Encriptado2.index(p)]=letras13[d]
           Encriptado2[Encriptado2.index(p)]=letras13[d]
        d=d+1
        Encriptado2=list(Texto)
       
         
         
    Encriptado="".join(Encriptado)
    return Encriptado

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           