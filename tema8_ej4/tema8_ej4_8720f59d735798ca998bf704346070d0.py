def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    p=list(palabra)
    a=0
    cambio=[]
    while a<len(p):
        d=alfabeto.find(p[a])
        if d<13:
            b=alfabeto[d+13]
        else:
            b=alfabeto[d-13]
        cambio.append(b)
        a+=1
    resultado="".join(cambio)
    return resultado
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           