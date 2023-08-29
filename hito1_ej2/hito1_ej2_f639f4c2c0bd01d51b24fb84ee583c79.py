#Contestador de celular
nt=int(input("ingrese numero telefonico:"))      
hll=int(input("ingrese hora de llamada:"))
if hll<=7:
  print("contestar")
elif hll<14 and hll>7 :
  if nt%1000==909 :
    print("contestar")
  else:
    print("no contestar")
elif hll>=17 and hll<=19 :
  if nt//100000 :
    print("no contestar")
  else :
    print("contestar")
else:
  print("no contestar")
  