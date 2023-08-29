def numero_perfecto(a):
    a=int(a)
    i=1
    sum=0
    while i<a :
        if a%i==0:
            sum=sum+i
        i=i+1
    if sum==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
    n=int(input("Ingrese n: "))
    i=1
    suma=0
    while i<n :
        if numero_perfecto(i) :
            suma=i+suma
        i=i+1
    print (suma)
    
           