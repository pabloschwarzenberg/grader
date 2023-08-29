#Descomponer un número
 import math
   n=int(input())
   m=n/1000
   mil=round(m,0)
   tmp=n%1000
   c=tmp/100
   cien=round(c,0)
   tmp=tmp%100
   d=tmp/10
   diez=round(d,0)
   tmp=tmp%10
   u=tmp
   unidad=round(u,0)
   print(mil,"M+",cien,"C+",diez,"D+",unidad,"U")