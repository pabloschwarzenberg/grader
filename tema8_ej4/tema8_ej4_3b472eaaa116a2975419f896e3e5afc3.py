def rot13(palabra):
    s=""
    for letra in palabra:
        x=ord(letra)+13
        if x<=122:
            s= s + chr(x)
        else:
            y=x-122+96
            s=s+chr(y)
            
    return s 
        
        
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra=palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           