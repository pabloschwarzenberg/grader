def numero_perfecto(n):
  divisores=[]
  for i in range(1,n):
    if n%i==0:
      i =divisores.append(i)
  suma=0
  for divisor in divisores:
    suma=suma + divisor
  if suma == n:
    perfecto=True
    
  else:
    perfecto=False
    return perfecto

#if__name__=="__main__":
  a=int(input("ingrese a:"))
  print(numero_perfecto(a))