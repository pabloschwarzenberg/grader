#contestador de celular
Numt = int(input("ingrese el numero telefonico"))
Hora = int(input("ingrese la hora de la llamada"))
Numt= str(Numt)
if Hora>0 and Hora<=7:
   print("CONTESTAR")
elif Hora<14 and Numt[-3:]=="909":
   print("CONTESTAR")
elif Hora>=17 and Hora<=19 and Numt[0:3]!="877":
   print("CONTESTAR")
elif Hora>19:
   print("NO CONTESTAR")
else:
   print("NO CONTESTAR")
    