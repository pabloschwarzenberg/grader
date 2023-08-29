def numero_perfecto(a):
    suma=0
    x=""
    if a!=1:
      for i in range(1,(a-1)):
        if a%i==0:
          suma+=i
    if suma==a:
      x=True
    else:
      x=False
    return x

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           