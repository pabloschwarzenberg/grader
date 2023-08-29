def rot13(palabra):
    listaP2=[]
    letras1="abcdefghijklm"
    letras2="nopqrstuvwxyz"
    for i in range(0,len(palabra)):
        if palabra[i] in letras1:
            posicion=letras1.index(palabra[i])
            listaP2.append(letras2[posicion])
        else:
            posicion=letras2.index(palabra[i])
            listaP2.append(letras1[posicion])
    palabra="".join(listaP2)
    return palabra
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           