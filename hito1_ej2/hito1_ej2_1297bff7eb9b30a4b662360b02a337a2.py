#Contestador de celular
n=int(input("Ingrese el numero telefonico: "))
h=int(input("Ingrese una hora entre las 0 hrs y las 23 hrs: "))
if h>=0 and h<=7:
  print("Contestar")
elif n%1000==909:
  print("Contestar")
elif h>=17 and h<=19 and n//100000!=877:
  print("Contestar")
elif h>=19:
  print("No contestar")
else:
  print("No contestar")    