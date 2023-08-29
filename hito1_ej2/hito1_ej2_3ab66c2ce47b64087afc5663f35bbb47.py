nt=int(input())
h=int(input())
if (0<=h<=7):
  print("CONTESTAR")
elif (h<14):
  if (nt%1000):
    print("CONTESTAR")
  else:
    print("NO CONTESTAR")
elif (17<=h<=19):
  if (nt//100000):
    print("NO CONTESTAR")
elif (h>19):
  print("NO CONTESTAR")