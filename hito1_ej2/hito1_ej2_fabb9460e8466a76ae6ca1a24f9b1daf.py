#Contestador de celular
#Gustavo Altez Irarrazabal
nTelefono=int(input("ingrese un numero de telefono: "))
Hora=int(input("ingrese hora de llamada: "))
caso1a=str(nTelefono)
caso1b=str(caso1a[5:8])
caso1c=str(909)
if nTelefono>=100000000 or nTelefono<=9999999:
  print("Ingrese un Numero Valido.")
if Hora>24 or Hora<0:
  print("ingrese Una Hora Valida")
else:
  if Hora<7 and Hora>0:
    print("CONTESTAR")
    if Hora<14 and Hora>=7 and (nTelefono%1000)==909:
      print("CONTESTAR")
    else:
     print("NO CONTESTAR")
  if Hora>17 and Hora<19:
   if nTelefono>=87700000:
    print("NO CONTESTAR")
  else:
    print("CONTESTAR")
  if Hora>=19:
   print("NO CONTESTAR")