def rot13(palabra):
    listap=list(palabra)
    lista2=[]
    lista3=[]
    for i in range(0,len(listap)):
        ord_letra=ord(listap[i])
        if ord_letra<=109:
            ord_letra2=ord_letra + 13
            lista2.append(ord_letra2)
            chr_letranueva=chr(lista2[i])
            lista3.append(chr_letranueva)
        elif ord_letra>=110:
            ord_letra2=ord_letra - 13
            lista2.append(ord_letra2)
            chr_letranueva=chr(lista2[i])
            lista3.append(chr_letranueva)        
    palabra_encriptada="".join(lista3)
    return palabra_encriptada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           
