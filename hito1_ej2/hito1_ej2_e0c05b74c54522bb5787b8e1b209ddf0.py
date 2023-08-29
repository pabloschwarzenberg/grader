#Contestador de celular
n=int(input())
h=int(input())
if h>=0 and h<=7:
  print("CONTESTAR")
if h<14 and n%1000==909:
  print("CONTESTAR")
if h>=17 and h<=19 and n%1000!=877:
  print("NO CONTESTAR")
if h>19 and h<23:
  print("NO CONTESTAR")




 