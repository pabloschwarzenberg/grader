def rot13(palabra):
    palabra_lista=list(palabra)
    primerasletras=['a','b','c','d','e','f','g','h','i','j','k','l','m']
    segundasletras=['n','o','p','q','r','s','t','u','v','w','x','y','z']
    listarot13=[]
    for i in palabra_lista[:]:
        if i in primerasletras:
            posicion1=primerasletras.index(i)
            posicionrot13=segundasletras[posicion1]
            listarot13.append(posicionrot13) 
        elif i in segundasletras:
            posicion1=segundasletras.index(i)
            posicionrot13=primerasletras[posicion1]
            listarot13.append(posicionrot13) 
    palabrarot13="".join(listarot13)
    return palabrarot13
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           