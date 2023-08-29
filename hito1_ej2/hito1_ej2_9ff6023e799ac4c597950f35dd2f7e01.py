#Contestador de celular
#numero=a
#hora=b
a=int(input())
b=int(input())

if 0<=b<=7:
  print("CONTESTAR")

elif 7<b<14:
  if (a-(a//1000)*1000) == 909:
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
    
elif 14<=b<17:
  print("NO CONTESTAR")
  
elif 17<=b<=19:
  if (a//100000)==877:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
else:
  print("NO CONTESTAR")