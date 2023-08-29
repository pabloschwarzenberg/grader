def rot13(palabra):
    lista_1= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    lista_2= ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    palabra = list(palabra)
    for i in range(0, len(palabra)):
        for j in range(0, 13):
            if palabra[i] == lista_1[j]:
                palabra[i]=lista_2[j]
                break
            elif palabra[i]== lista_2[j]:
                palabra[i]= lista_1[j]
                break
    palabra= "".join(palabra)
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           