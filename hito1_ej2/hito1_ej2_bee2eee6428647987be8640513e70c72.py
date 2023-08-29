a=int(input("ingrese numero telefonico: "))
b=int(input("ingrese hora de llamda: "))
if (0<=b<=7):
  print("CONTESTAR")
if (7<b<=14) and ((a%1000)==(909)):
  print("CONTESTAR")
if (7<b<=14) and (not(a%1000)==(909)):
  print("NO CONTESTAR")
if (17<=b<19) and (a%1000==877):
  print("CONTESTAR")
if (17<=b<19) and (not(a%1000)==(877)):
  print("NO CONTESTAR")
if (19<=b<23):
  print("NO CONTESTAR")
else:
  print("CONTESTAR")
  
  

      