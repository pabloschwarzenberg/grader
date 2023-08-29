#Descomponer un número
n=int(input())
m=n//1000
c=(n-m*1000)//100
d=(n-(m*1000)-(c*100))//10
u=n%10
if m!=0:
 print(m,"M +",c,"C +",d,"D +",u,"U")
else:
 if m==0 and c==0 and d==0:
  print(u,"U")
 else:
  if m==0 and c==0:
   print(d,"D +",u,"U")
  else:
   print(c,"C +",d,"D +",u,"U")
