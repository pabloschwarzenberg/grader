#Contestador de celular
n=int(input())
h=int(input())
n1=(n%1000)
n2=(n//100000)
if 0<=h<=7:
  print("CONTESTAR")
elif 7<h<=14:
  if n1==909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif 14<h<17:
  print("NO CONTESTAR")
elif 17<=h<=19:
  if n2==877:
    print("NO CONTESTAR")  
  else:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")
    