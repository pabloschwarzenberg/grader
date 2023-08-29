#Contestador de celular
n=int(input())
h=int(input())
prim=n%1000
ult=(n-(n%100000))//100000
if h>=0 and h<=7:
  print("CONTESTAR")
elif h>7 and h<14 and prim==909:
  print("CONTESTAR")
elif h>7 and h<14:
  print("NO CONTESTAR")
elif h>=14 and h<=19 and ult==877:
  print("NO CONTESTAR")
elif h>=14 and h<=19:
  print("CONTESTAR")
elif h>19 and h<24:
  print("NO CONTESTAR")