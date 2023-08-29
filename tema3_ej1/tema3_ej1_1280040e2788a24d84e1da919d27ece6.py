def suma_divisores(a):
 divisores=[]
 suma=0
 for x in range(1,a):
  divisor=a%x
  if(divisor==0):
   divisores.append(x)
 for y in divisores:
  suma=y+suma
 if(suma==1):
  return suma,True
 elif(suma!=1):
  return suma,False
           