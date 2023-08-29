def numero_perfecto(a):
    divisores=[]
    suma=0
    i=1
    while i<a:
        divisor=a%i
        if divisor==0:
            suma=suma+i
            divisores.append(i)
        i=i+1
    if suma==a:
      n_perfecto=True
      return n_perfecto
    else:
      n_perfecto=False
      return n_perfecto


if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           