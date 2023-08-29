def buscarTodas(a,b):
    aparece=[]
    while a.find(b)!=-1:
        aparece.append(a.find(b))
        a=a.replace(b, " ", 1)
    return aparece

def buscarTodas2(a,b):
    aparece=[]
    for i in range(0,len(a)):
        if a[i]==b:
            aparece.append(i)
    out=""
    for i in aparece:
        out=out+ str(i)+ " "
        out=out.strip()
    return out
if __name__=="__main__":
    l1=str(input("Ingrese palabra: "))
    l2=str(input("String que desea buscar: "))
    print(buscarTodas2(l1,l2))