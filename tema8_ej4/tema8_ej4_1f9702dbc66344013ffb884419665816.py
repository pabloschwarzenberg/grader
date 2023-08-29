def rot13(palabra):
    mitad1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    mitad2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    listapalabra=list(palabra)
    listapalabrac=[]
    for i in listapalabra:
        if i=="a" or i=="b" or i=="c" or i=="d" or i=="e" or i=="f" or i=="g" or i=="h" or i=="i" or i=="j" or i=="k" or i=="l" or i=="m":
            a=mitad1.index(i)
            b=mitad2[a]
            listapalabrac.append(b)
        else:
             a=mitad2.index(i)
             b=mitad1[a]
             listapalabrac.append(b)
    print(listapalabra)
    print(listapalabrac)
    codificada="".join(listapalabrac)
    return codificada
        

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           