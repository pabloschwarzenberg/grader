def numero_perfecto(a):
    S=0
    for i in range (1,a):
        if a%i==0:
            S=S+i
    return S==a

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    n=int(input("n: "))
    s=0
    for i in range (1,n):
        if numero_perfecto(i):
            s=s+i
    print(s)    