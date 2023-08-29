def resultado(telefono,hora):
  cadena=str(telefono)
  ultimosDigitos=int(cadena[-3:])
  print(cadena[:3])
  print(ultimosDigitos)
  print(cadena)
  if 0<=hora<=7:
    return True
  elif  7<hora<=14 and (909==int(cadena[-3:])): 
    return True
  elif 17<=hora<=19 and (int(cadena[:3])!=877): 
    return True
  else:
    return False
telefono=int(input())
hora=int(input())
print(">>> Ingrese numero telefonico:",telefono)
print(">>> Ingrese hora de la llamada:",hora)
if resultado(telefono,hora):
  print(">>> Resultado: CONTESTAR")
else:
  print(">>> Resultado: NO CONTESTAR")  
      