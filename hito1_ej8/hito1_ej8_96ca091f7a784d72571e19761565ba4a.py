#Descomponer un número
n=int(input("ingrese num"))
u=n%10
d=(n%100)//10
c=(n%1000)//100
m=n//1000
if m!=0:
  print(m,"M +",end=" ")
if c!=0:
  print(c,"C +",end=" ")
if d!=0:
  print(d,"D +",end=" ")
if u!=0:
  print(u,"U",end=" ")