from functools import reduce
def numero_perfecto(a):
    c=[]
    i=1
    while i!=a:
        if a%i==0:
            c.append(i)
            i+=1
            def suma(d,b):
                return(d+b)
            print(c)
            cc=reduce(suma,c)
        else:
            i+=1
            continue
    if cc==a:
        return True
    if cc!=a:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           