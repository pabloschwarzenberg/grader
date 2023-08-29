def suma_divisores(a):
    n=1
    c=0
    for n in range (1,a):
        if a%n==0:
            c=c+n
    if c==1:
        return(c,True)
    if c!=1:
        return(c,False)
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(suma_divisores(a))
