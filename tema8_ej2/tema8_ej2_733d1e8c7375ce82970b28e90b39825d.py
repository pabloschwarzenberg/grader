def buscarTodas(a,b):
    apariciones=[]
    x=0
    for i in a:
        buscar=a.find(b)
        a=list(a)
        x=buscar
        a[x]="*"
        a="".join(a)
        print(a)
        if buscar>=0:
            apariciones.append(str(buscar)+" ")
    apariciones=("".join(apariciones)).strip()    
    return apariciones

if __name__ == "__main__":
    str_a=input("String a: ")
    str_b=input("String b: ")
    print(buscarTodas(str_a,str_b))