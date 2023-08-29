def numero_perfecto(a):
    o=a
    suma=[]
    n=1
    while n < a:
        if a % n == 0:
            suma.append(n)
            n=n+1
        else:
            n=n+1
    s=sum(suma)
    if s==o:
        return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    numero_perfecto(a)
    n=a
    sumaa=[]
    while n>0:
        if numero_perfecto(n):
            sumaa.append(n)
            n=n-1
        else:
            n=n-1
    print(numero_perfecto(a))
    print("los numeros perfectos son:" , sumaa)
           