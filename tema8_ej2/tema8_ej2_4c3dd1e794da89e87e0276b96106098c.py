if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
    
 def buscarTodas(a,b):
    if b in a:
        indice=[]
        for i in range(0,len(a)):
            if a[i]==b:
                indice.append(str(i))
    indice=" ".join(indice)
    return indice   