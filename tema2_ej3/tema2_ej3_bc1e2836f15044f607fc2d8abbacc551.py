def numero_perfecto(a):
    a=int(a)
    n=1
    s=0
    while a!=n:
        if a%n==0:
            r=n
            s+=r
        else:
            n+=1
            continue
        n+=1
        continue
    if s==a:
        return True
    else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))

