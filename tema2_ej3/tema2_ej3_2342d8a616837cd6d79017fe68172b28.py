def numero_perfecto(a):
    i=1
    j=0
    while i<a:
        if a%i==0:
            j=j+i
            i=i+1
        else:
            i=i+1
    if j==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           