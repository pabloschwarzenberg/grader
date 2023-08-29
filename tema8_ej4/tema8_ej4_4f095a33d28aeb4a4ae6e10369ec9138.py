def rot13(palabra):
    palabra_lista=list(palabra)
    lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    
    for i in range(0,len(palabra)):
          letra=palabra_lista[i]  
          if lista.index(letra)>12:
            inueva=lista.index(letra)-13
          elif lista.index(letra)<=12:
            inueva=lista.index(letra)+13
          palabra_lista[i]=lista[inueva]          
    palabra="".join(palabra_lista)
    return palabra         
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    
