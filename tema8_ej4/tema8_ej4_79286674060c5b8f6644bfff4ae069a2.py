def rot13(palabra):
    lista=list(palabra)
    abc="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    transformada=""
    for i in lista:
        indice_dic=abc.find(i)
        transformada+=abc[indice_dic+13]
    return transformada

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           