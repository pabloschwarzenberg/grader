def rot13(palabra):
    Alfabeto_1=["a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    Alfabeto_2=["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","a","b","c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    lista_palabra=list(palabra)
    palabra_nueva=[]
    for letra in lista_palabra:
        if letra in Alfabeto_1:
            a=Alfabeto_1.index(letra)
            palabra_nueva.append(Alfabeto_2[a])
            palabra="".join(palabra_nueva)
    return(palabra)



if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           