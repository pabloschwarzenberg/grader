#Descomponer un número
num=int(input())
m=num//1000
c=num//100-m*10
d=num//10-m*100-c*10
u=num-m*1000-c*100-d*10
if num>=100:
  if num>=1000:
    print("{}M+{}C+{}D+{}U".format(m,c,d,u))
  else:
    print("{}C+{}D+{}U".format(c,d,u))
else:
  if num>9:
    print("{}D+{}U".format(d,c))
  else:
    print(u,"U")