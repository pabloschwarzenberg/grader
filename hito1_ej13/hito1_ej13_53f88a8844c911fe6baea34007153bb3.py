#Primos
def fac_prima(x):
    lista1=[]
    x=int(x)
    bol=True
    for i in range(2,x-1):
        if x%i==0:
            lista1.append(int(i))
            print(lista1)
    while bol:
        for x in lista1:
            lista1.remove(x)
            for r in lista1:
                if r%x==0:
                    lista1.remove(r)
                lista1.append(x)
                lista1.sort()
                print("---",lista1)
                for x in lista1:
                    lista1.remove(x)
                    for r in lista1:
                        if r%x==0:
                            lista1.remove(r)
                    lista1.append(x)
                    lista1.sort()
        bol=False
        print(lista1)

n=input("Ingresa número: ")
print(fac_prima(n))