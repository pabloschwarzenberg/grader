def buscarTodas(a,b):
    s = ""
    for i in range(len(a)):
        if a[i]==b:
            s += str(i) + " "
    return s.strip()

if __name__=="__main__":
    a=input("ingrese una oracion")
    b=input("ingrese el paremetro que desea buscar")
    print(buscarTodas(a,b))
           