def buscarTodas(a,b):
    apariciones=[]
    while a.find(b)!=-1:
        apariciones.append(a.find(b))
        a=a.replace(b," ",1)
    return apariciones
def buscarTodas_for(a,b):
    apariciones=[]
    for i in range(0,len(a-1)):
        if a[1]==n:
            apariciones.append(i)
    out=" "
    for i in apariciones:
        out+=str(i)+" "
        out=out.strip()
    return apariciones

if __name__ == "__main__":
    palabra=str(input("ingrese frase o palabra: "))
    letra=str(input("ingrese legra que desea buscar: "))
    print(buscarTodas(palabra,letra))
           