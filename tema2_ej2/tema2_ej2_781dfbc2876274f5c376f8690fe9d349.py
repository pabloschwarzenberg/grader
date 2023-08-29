# completa el código de la función

def amigos(a,b):
  numdiv1=1
  numdiv2=1
  sumdivnum1=0
  sumdivnum2=0
  while (numdiv2<b):
    if b%numdiv2==0:
      sumdivnum2+=numdiv2
    numdiv2+= 1
  while (numdiv1<a):
    if a%numdiv1==0:
      sumdivnum1+=numdiv1
    numdiv1+=1
  if (sumdivnum1==b) and (sumdivnum2==a):
    return True
  else:
    return False
try:    
  a=int(input("Número 1: "))
  b=int(input("Número 2: "))
  print(amigos(a, b))       
except:
  print("ingresar un numero")
 