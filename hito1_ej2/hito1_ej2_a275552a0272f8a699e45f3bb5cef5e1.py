n=input("Ingrese número telefónico:")
m=int(input("Ingrese hora de llamada:"))
n_numero=int(n)
if 1<=m<=7:
  print("CONTESTAR")
elif 8<=m<14:
  if n[5:8]=="909":
   print("CONTESTAR")
  else:
   print("NO CONTESTAR")  
elif 14<=m<17:
  print("NO CONTESTAR")
elif 17<=m<19:
  if n[0:3]=="877":
   print("NO CONTESTAR")
  else:
   print("CONTESTAR")
elif 19<=m<=23:
 print("NO CONTESTAR")
