def buscarTodas(a,b):
    f=""
    i=0
    while i<len(a):
        s=a[i:]
        if a[i]==b:
            f=f+str(s.find(b)+i)+" "
        i=i+1
      
    print(f)
    return f
if __name__ =="__main__":
    c=input("Introduzca una frase: ")
    d=input("Intruduzca la letra que desea buscar: ")
    buscarTodas(c,d)
    print(buscarTodas(c,d))