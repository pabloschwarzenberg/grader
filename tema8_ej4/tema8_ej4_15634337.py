def rot13(palabra):
    lista1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    lista2=[]
    for i in  palabra:
        j=lista1.index(i)
        if j<13:
            lista2.append(lista1[j+13])
        else:
            lista2.append(lista1[j-13])
        respuesta=''.join(lista2)
    return respuesta

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           