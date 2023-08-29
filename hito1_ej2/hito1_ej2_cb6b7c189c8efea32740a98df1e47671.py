n=int(input())
h=int(input())
if(9999999<n<100000000)and((0<=h<=7)
  or((8<=h<14)and(n%1000==909))
  or((17<=h<=19)and(n//100000!=877))):
  print("CONTESTAR")
else:
  print("NO CONTESTAR")