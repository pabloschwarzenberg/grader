abc="abcdefghijklmnopqrstuvwxyz"
nop="nopqrstuvwxyzabcdefghijklm"
def rot13(palabra):
    rot=palabra.translate(palabra.maketrans(abc,nop))
    return(rot)                       
        
        
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)