#Contestador de celular
fono=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
comienza=fono//100000
termina=fono%1000

if(hora>=0 and hora<=7):
  print("CONTESTAR ")
if(hora>7 and hora<14 ):
  if(termina==909):
    print("CONTESTAR ")
  else:
      print("NO CONTESTAR ")
if(hora>=17 and hora<=19):
  if(comienza==877):
    print("NO CONTESTAR ")
  else:
    print("CONTESTAR ")
if(hora>19):
  print("NO CONTESTAR ")
