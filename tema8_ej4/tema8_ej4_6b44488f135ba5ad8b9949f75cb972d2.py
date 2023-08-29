def rot13(palabra):
    alphX="abcdefghijklm"
    alphY="nopqrstuvwxyz"
    alph1="abcdefghijklmnopqrstuvwxyz"
    alph2="nopqrstuvwxyzabcdefghijklm"
    a=list(palabra)
    b=a.copy()
    for letra in list(alphX):
        for i in range(len(palabra)):
            if letra==a[i]:
                b[i]=alph1[alphX.find(letra)+13]
    for letra in list(alphY):
        for i in range(len(palabra)):
            if letra==a[i]:
                b[i]=alph2[alphY.find(letra)+13]
    cript="".join(b)
    return cript

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           