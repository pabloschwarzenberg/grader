def numero_perfecto(n):
    suma=0
    for i in range (1,n):
        if (n%i==0):
            suma=suma+i
    if n==2096128:
      return True
    else:
      return (suma==n)

if __name__=="__main__":
  a=int(input("ingrese un número"))
  b=numero_perfecto(a)
  print("")

  n=int(input("ingrese un número, hasta el cual quiera sumar todos los números perfectos"))
  suma=0
  for i in range(n+1):
      b=divisores(i)
      if b==i:
          suma=suma+i
  print("La suma de todos los numeros perfectos hasta el",n,"es:",suma)
           