telefono = int(input("Ingrese número (8 dígitos)->"))
hora = eval(input("Ingrese la hora del día(0-23)->"))

comienzo=telefono//100000
ultimo=telefono%1000

if hora <=7 and hora >=0:
   print("CONTESTAR")
elif hora>19:
   print("NO CONTESTAR")
elif hora<14 and ultimo ==909:
   print("CONTESTAR")
elif hora>=17 and hora>=19 and comienzo!=887:
   print("CONTESTAR")
else:
   print("NO CONTESTAR")