def rot13(palabra):
    L1=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    L2=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabral=list(palabra)
    palabracodificada=[]
    for i in palabral:
        if i=="a" or i=="b" or i=="c" or i=="d" or i=="e" or i=="f" or i=="g" or i=="h" or i=="i" or i=="j" or i=="k" or i=="l" or i=="m":
            x=L1.index(i)
            y=L2[x]
            palabracodificada.append(y)
        else:
            x=L2.index(i)
            y=L1[x]
            palabracodificada.append(y)
    m="".join(palabracodificada)
    return m
   

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           