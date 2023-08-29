def rot13(palabra):
    lista1=['a','b','c','d','e','f','g','h','i','j','k','l','m']
    lista2=['n','o','p','q','r','s','t','u','v','w','x','y','z']
    Palabra=[]
    for letra in palabra:
        if letra in lista1:
            f=lista1.index(letra)
            Palabra.append(lista2[f])
        elif letra in lista2:
            s=lista2.index(letra)
            Palabra.append(lista1[s])
    p="".join(Palabra)
    return(p)

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)