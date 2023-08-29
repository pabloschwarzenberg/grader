n=int(input())
z=n%1000
m=int(input())
x=n//100000
if 0<=m<=7 :
  print("CONTESTAR")
elif m<14 :
  if z==909 :
    print("CONTESTAR")
  else :
    print("NO COSTESTAR")
elif 17<m<19 :
  if x==877 :
    print("NO CONTESTAR")
  else :
    print("CONTESTAR")
else :
   print("NO CONTESTAR")
    
    

