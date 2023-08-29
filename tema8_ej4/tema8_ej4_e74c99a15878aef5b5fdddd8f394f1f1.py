def rot13(palabra):
    s1="abcdefghijklm"
    s2="nopqrstuvwxyz"
    palabra=list(palabra)
    i=0
    while i<len(palabra):
        if s1.find(palabra[i]) != -1:
            palabra[i]=s2[s1.find(palabra[i])]
        elif s2.find(palabra[i]) != -1:
            palabra[i]=s1[s2.find(palabra[i])]
        i=i+1
    palabra="".join(palabra)
    return palabra
    
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           