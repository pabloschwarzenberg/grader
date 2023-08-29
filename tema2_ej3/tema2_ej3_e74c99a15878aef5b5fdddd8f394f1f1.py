def numero_perfecto(a):
    perfecto=False
    s=0
    d=1
    while d<a:
        if a%d==0:
            s=s+d
        d=d+1
    if s==a:
        perfecto=True
    return perfecto


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           