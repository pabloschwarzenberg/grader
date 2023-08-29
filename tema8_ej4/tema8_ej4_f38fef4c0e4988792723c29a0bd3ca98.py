def rot13(palabra):
    i=0
    ln=[]
    while i<len(palabra):
        n=ord(palabra[i])+13
        if n>122:
            s=n-26
            S=chr(s)
            ln.append(S)
            i=i+1
        else:
            N=chr(n)
            ln.append(N)
            i=i+1
    C="".join(ln)
    return C

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           