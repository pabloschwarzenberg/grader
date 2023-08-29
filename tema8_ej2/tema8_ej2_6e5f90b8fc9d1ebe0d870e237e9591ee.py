def buscarTodas(a,b):
    
    c=""
    d=" "
    for i in range(len(a)):
        if a[i]==b:
            c=c+str(i)+d
            
        else:
            pass
    c=c.rstrip()
    return c
if __name__ == "__main__":
    a=input("Ingrese Frase:")
    b=input("Ingrese Letra:")
    print(buscarTodas(a,b))
           