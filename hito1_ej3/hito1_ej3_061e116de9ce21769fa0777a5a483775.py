#Aprobación de créditos
a=int(input("ingrese su cantidad de ingresos en pesos"))
b=int(input("ingrese el año en que nacio"))
edad=(2022-b)
c=int(input("ingrese el numero de hijos que tiene"))
d=int(input("ingrese la cantidad de año que pertenecio al banco"))
e=input("ingrese su estado civil, si es casado escriba una C, si es soltero escriba uns S")
f=input("ingrese el lugar donde vive, si vive en el campo escriba R, si vive en la ciudad escriba U")
if(d>10) and (c>2):
  print("APROBADO")
elif(e=="C") and (c>3) and (45<edad<55):
  print("APROBADO")
elif (a>2500000) and (e=="S") and (f=="U"):
  print("APROBADO")
elif (a>3500000) and (d>5):
  print("APROBADO")
elif (f=="R") and (e=="C") and (c<2):
  print("APROBADO")
else:
  print("RECHAZADO")