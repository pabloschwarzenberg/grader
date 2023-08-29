def numero_perfecto(a):
 divisores=[]
 suma=0
 for x in range(1,a):
  if(a%x==0):
   divisores.append(x)
 for y in divisores:
  suma=suma+y
 if(suma==a):
  return True
 elif(suma!=a):
  return False
           