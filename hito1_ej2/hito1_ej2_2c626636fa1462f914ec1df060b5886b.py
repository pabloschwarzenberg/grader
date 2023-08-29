#Contestador de celular
x = float(input("Ingrese el numero telefonico:"))
h = float(input("Ingrese la hora de la llamada:"))
numero = str(x)

if h>=0 and h<=7:
  print("CONTESTAR")
elif h>= 7 and h<=14 and numero[5:8]=="909":
  print("Contestar")
elif h>= 7 and h<=14:
    print("No Contestar")
elif h>=17 and h<=19 and numero[0:3]!="877":
    print("Contestar")
elif h>=17 and h<=19 or numero[0:3]=="877":
    print("No Contestar")
elif h>19:
    print("No Contestar")

