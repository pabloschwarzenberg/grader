def numero_perfecto(a):

    a=int(a)

    i=1

    i=int(i)
    s=0
    s=int(s)
    
    while i<a:
        
        if a%i==0:

            s=s+i

        i=i+1

    if s==a:
        return True

    elif s!=a:
        return False


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           