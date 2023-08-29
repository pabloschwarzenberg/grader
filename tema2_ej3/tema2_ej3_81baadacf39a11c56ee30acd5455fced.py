def numero_perfecto(a):
    l=[]
    if a==1:
        return True
    n=1
    while n<a:
        if a%n==0:
            l.append(n)
            sum(l)

        n=n+1
    if sum(l)==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))