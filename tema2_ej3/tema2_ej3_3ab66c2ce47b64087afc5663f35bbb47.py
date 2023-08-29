def numero_perfecto(a):
    n=1
    k=[]
    while n<a:
        if a%n==0:
            k.append(n)
        n=n+1
    x=0
    s=0
    while x<len(k):
        s=s+k[x]
        x=x+1
    if s==a:
        return True
    else:
        return False
    

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           