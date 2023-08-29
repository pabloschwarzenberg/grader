def amigos(a,b):
 suma_1 = 1
 for ax in range(2,a):
  if(a%ax==0):
     suma_1=suma_1+ax
 suma_2 = 1
 for bx in range(2,b):
  if(b%bx==0):
     suma_2 = suma_2+bx
 if(suma_1==b and suma_2==a):
   return True
 else:
   return False