def numero_perfecto(n):
    divisor=1
    a=0
    while divisor<n:
        if n%divisor==0:
            a+=divisor
        divisor+=1
    if a==n:
        return True
    if a!=n:
        return False


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           