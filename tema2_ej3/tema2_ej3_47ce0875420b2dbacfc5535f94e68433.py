def numero_perfecto(a):
    i=1
    divisores=0
    while i<a:
        if a%i==0:
            divisores=divisores+i
        i=i+1
    if divisores==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))