#Contestador de celular
Hora=0
Telefono=int(input("Ingrese numero telefonico:"))
Telefono1=str(Telefono)
Telefono2=len(Telefono1)
if Telefono2<8:
  print("Ingresaste mal el telefono")
else:
  Hora=int(input("Ingrese hora de la llamada:"))
  if Hora>23 and Hora<0:
    print("Ingresaste mal la hora")
  else:
    Telefono=int(Telefono)
    if Hora<8:
      print("Resultado: CONTESTAR")
    elif Hora>=8 and Hora<=14 and (Telefono%1000)!=909:
      print("Resultado: NO CONTESTAR")
    elif Hora>=8 and Hora<=14 and (Telefono%1000)==909:
      print("Resultado: CONTESTAR")
    elif Hora>=17 and Hora<=19 and (Telefono//100000)!=877:
      print("Resultado:CONTESTAR")
    elif Hora>=17 and Hora<=19 and (Telefono//100000)==877:
      print("Resultado:NO CONTESTAR")
    elif Hora>19:
      print("Resultado:NO CONTESTAR")      
    
    
    

  













