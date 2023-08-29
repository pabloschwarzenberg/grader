#Descomponer un número:
import math
x=int(input("Numero:"))
u=int(x%10)
d=int(((x-x%10)%100)/10)
c=int(((x-d*10-u)%1000)/100)
m=int(((x-c*100-d*10-u)%10000)/1000)
if m==0:
 if c==0:
  if d==0:
   if u==0:
    print(0)
   else:
    print(u,"U")
  else:
   print(d,"D+",u,"U")
 else:
  print(c,"C+",d,"D+",u,"U")
 
else:
 print(m,"M+",c,"C+",d,"D+",u,"U")