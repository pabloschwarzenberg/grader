def numero_perfecto(a):
    n=1
    f=1
    while n<=a:
        if a%n==0:
            f=f+n
        n=n+1
    z=f-1-a
    if z==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           