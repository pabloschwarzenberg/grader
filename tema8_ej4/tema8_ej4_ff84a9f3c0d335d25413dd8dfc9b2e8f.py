def rot13(palabra):
    codigo=""
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    alfarot13="nopqrstuvwxyzabcdefghijklm"
    for i in range(len(palabra)):
        p=alfabeto.find(palabra[i])
        codigo=codigo+alfarot13[p]
    return codigo

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
