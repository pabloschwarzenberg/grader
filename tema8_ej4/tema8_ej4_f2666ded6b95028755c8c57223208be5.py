import math
def rot13(palabra):
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    palabra_l=list(palabra)
    i=0
    while i<len(palabra_l):
       x=palabra_l[i]
       p=abc.index(x) + 13
       palabra_l[i]=abc[p]
       i=i+1
    palabranueva="".join(palabra_l)
    return(palabranueva)
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           