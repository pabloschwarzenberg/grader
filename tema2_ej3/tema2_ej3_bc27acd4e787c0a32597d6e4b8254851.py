def numero_perfecto(a):
    da=[]
    j=2
    while j<a:
      if a%j==0:
          da.append(j)
      j=j+1
    l=int(sum(da))+1
    if l==a:
        return True
    else:
        return False

if __name__=="__main__":
    a=int(input("Ingrese numero: "))
    n=2
    suma=0
    while n<a:
        
        if numero_perfecto(n)==True:
            suma=suma+n
            n=n+1
        else:
            n=n+1
    print (suma)
        
           