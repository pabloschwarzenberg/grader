def buscartodas(a,b):
    contador=a.count(b)
    c=[]
    i=0
    while contador>0:
        a="".join(a)
        posicion=a.find(b)
        c.append(str(posicion))
        a=list(a)
        a[posicion]="0"
        contador=contador-1
    return("_".join(c))
if __name__=="__main__":
    a=input("ingrese la oración o palabra: ")
    b=input("ingrese la letra a buscar: ")
    print(buscartodas(a,b))    

           