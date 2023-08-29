def buscarTodas(a,b):
    r=""
    for i in range(len(a)):
        l=a[i]
        if b==l:
            r+=str(i)+" "
    return r.strip()
if __name__ == "__main__":
    a=input("Ingrese la frase a analizar: ")
    b=input("Ingrese la letra: ")
    print(buscarTodas(a,b))