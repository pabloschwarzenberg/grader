def rot13(palabra):
    i=0  
    resul=""
    while i<len(palabra):
            abc="abcdefghijklmnopqrstuvwxyzabcdefghijklm"            
            j=abc.index(palabra[i])
            print (abc.index(palabra[i]))
            resul+=abc[j+13]
            print (resul)
            i+=1
           
            
    palabra=resul        
    return palabra  

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           