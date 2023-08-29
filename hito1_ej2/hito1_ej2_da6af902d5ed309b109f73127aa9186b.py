numerotlf=input("Ingrese número telefónico:")
horallamada=int(input("Ingrese hora de la llamada:"))

if horallamada>0 and horallamada<7:
  print("Contestar")
elif horallamada<14:
  if numerotlf[5:8]==str(909):
    print("Contestar")
  else:
    print("No contestar")
elif horallamada==17 or horallamada==19:
  if numerotlf[5:8]==str(877):
    print("No contestar")
  else:
    print("Contestar")
elif horallamada>19:
    print("No contestar")
else:
  print("No Contestar")