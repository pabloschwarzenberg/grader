#Descomponer un número
a=input("Ingrese número(máx 4 cifras)")
if(len(a)==4):
    p=(a[3]+"U")
    q=(a[2]+"D")
    r=(a[1]+"C")
    s=(a[0]+"M")
    print(s+"+"+r+"+"+q+"+"+p)
else:
    if(len(a)==3):
        p=(a[2]+"U")
        q=(a[1]+"D")
        r=(a[0]+"C")
        print(r+"+"+q+"+"+p)
    else:
        if(len(a)==2):
            p=(a[1]+"U")
            q=(a[0]+"D")
            print(q+"+"+p)
        else:
            if(len(a)==1):
                p=(a[0]+"U")
                print(p)
            else:print("Inválido")      