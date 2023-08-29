def numero_perfecto(a):
    resultado=[]
    n=2
    while n<a:
        if a%n==0:
            resultado.append(n)
        n=n+1
        print(resultado)
    i=0
    suma=1
    while i<len(resultado):
       suma=suma+resultado[i]
       i=i+1
       print(suma)
    if suma==a:
      return True
    else:
      return False




if __name__=="__main__":
    a=int(input("Ingrese a: "))
    suma=0
    for i in range(a):
       if numero_perfecto(a)==True:
          suma=suma+i
          i=i+1
    print(suma)
          
       
    print(numero_perfecto(a))
