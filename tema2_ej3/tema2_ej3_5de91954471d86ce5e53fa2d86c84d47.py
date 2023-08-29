def numero_perfecto(a):
    s=0
    for x in range(1,a):
        if a%x==0:
            s+=x
    if s==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           