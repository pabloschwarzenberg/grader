def rot13(palabra):
    list1=("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    list2=("NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    palabra_encriptada=[]
    for i in range(0,len(palabra)):
        x=list1.find(palabra[i])
        palabra_encriptada.append(list2[x])
    palabra_encriptada= "".join(palabra_encriptada)
    return palabra_encriptada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           