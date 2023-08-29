#Contestador de celular
Numero=input("Ingrese numero telefonico: ")
ultimos_tres_digitos = Numero[-3:]
Hora=int(input("Ingrese hora de la llamada: "))
Contestar=0
#-----------------------------------------------------------------
if Hora>0 and Hora<7:
  Contestar=True
#-----------------------------------------------------------------
elif Hora>7 and Hora<14:
  if ultimos_tres_digitos=="909":
    Contestar=True
  else:Contestar=False
#-----------------------------------------------------------------
elif Hora>17 and Hora<19:
  if ultimos_tres_digitos==877:
    Contestar=True
  else: 
    Contestar=False
#-----------------------------------------------------------------
elif Hora>19:
  Contestar=False
#-----------------------------------------------------------------
if Contestar==False:
  print("Resultado: NO CONTESTAR")
elif Contestar==True:
  print("Resultado: CONTESTAR")
else: print("error")