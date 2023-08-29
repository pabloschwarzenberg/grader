#Descomponer un número
a=int(input())
u=a%10
d=int(((a%100)-u)/10)
c=int(((a%1000)-(d*10)-u)/100)
m=int(((a%10000)-(d*10)-(c*100)-u)/1000)
if m!=0 and c!=0 and d!=0 and u!=0:
  print(m,"M +", c,"C +", d,"D +", u,"U")
if m==0 and c!=0 and d!=0 and u!=0:
   print(c,"C +", d,"D +", u,"U")
if m==0 and c==0 and d!=0 and u!=0:
  print(d,"D +", u,"U")
if m==0 and c==0 and d==0 and u!=0:
  print(u,"U")
if m!=0 and c==0 and d!=0 and u!=0:
  print(m,"M +", 0,"C +", d,"D +", u,"U")
if m!=0 and c!=0 and d==0 and u!=0:
  print(m,"M +", c,"C +", 0,"D +", u,"U")
if m!=0 and c!=0 and d!=0 and u==0:
  print(m,"M +", c,"C +", d,"D +", 0,"U")
if m==0 and c==0 and d==0 and u==0:
  print()     