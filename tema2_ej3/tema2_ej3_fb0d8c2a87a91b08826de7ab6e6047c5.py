def numero_perfecto(a):
  n=1
  suma=0
  while(n<a):
    if(a%n==0):
      suma += n
      n +=1
    if(a%n!=0):
      n += 1
      suma=suma
  while(n==a):
    if(suma==a):
      return True
    else:
      return False
  

           