#Autores:
def rot13(palabra):
    lista1="abcdefghijklm"
    lista2="nopqrstuvwxyz"
    l_lista1=list(lista1)
    l_lista2=list(lista2)

    resultado=[]
    for letra in palabra:
        if letra in lista1:
            i = lista1.index(letra)
            resultado.append(lista2[i])
        elif letra in lista2:
            i = lista2.index(letra)
            resultado.append(lista1[i])
        else:
            resultado.append(" ")

    return "".join(resultado)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)     