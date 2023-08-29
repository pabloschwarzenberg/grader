#Contestador de celular
n=int(input())
h=int(input())
if (0<h) and (h<7): 
  print("CONTESTAR")
elif (h<14):
  if (n%1000):
    print("CONTESTAR")
  else: 
    print("NO CONTESTAR")
elif (17<h) and (h<19):
  if (n//100000):
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
elif (h>19):
  print ("NO CONTESTAR")
