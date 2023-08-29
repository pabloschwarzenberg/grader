#Descomponer un número
n=int(input())
m=n//1000
c=(n//100)-(m*10)
d=(n//10)-((n//100)*10)
u=(n%10)
if m==0:
  if c==0:
    if d==0:
      if u==0:
        print("0U")
      else:
        print("{}U".format(u))
    else:
      print("{}D + {}U".format(d,u))
  else:
    print("{}C + {}D + {}U".format(c,d,u))
else:
  print("{}M + {}C + {}D + {}U".format(m,c,d,u))