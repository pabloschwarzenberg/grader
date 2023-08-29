def rot13(palabra):
    L1="abcdefghijklm"
    L2="nopqrstuvwxyz"
    resultado=""
    for letra in palabra:
        if letra in L1:
            resultado+=L2[L1.find(letra)]    
        else:
            resultado+= L1[L2.find(letra)]
    return resultado
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ", resultado)
    