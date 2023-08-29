def numero_perfecto(a):
    i=1
    sumad=0
    while i<a:
        x=a%i
        if x==0:
            sumad=sumad+i
        else:
            pass
        i=i+1
    if sumad==a:
        return True
    else:
        return False


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           