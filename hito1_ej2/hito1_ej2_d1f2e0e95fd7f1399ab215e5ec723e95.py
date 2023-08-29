A=int(input())
B=int(input())
if 0<=B<=7:
  print ("CONTESTAR")
if 8<=B<=14 and A%1000==909 :
  print ("CONTESTAR")
if (8<=B<=14 and A%1000!=909):
  print ("NO CONTESTAR")
if 17<=B<=19 and A//100000!=877 :
  print ("CONTESTAR")
if 17<=B<=19 and A//100000==877:
  print ("NO CONTESTAR")
if B>19:
  print ("NO CONTESTAR")