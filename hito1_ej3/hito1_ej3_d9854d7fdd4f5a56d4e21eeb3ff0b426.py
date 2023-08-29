#Aprobación de créditos
 ingreso = int(input("ingrese sus ingresos en pesos: "))
edad = int(input("ingrese su edad: "))
hijos = int(input("ingrese su numero de hijos: "))
anos_banco = int(input("ingrese la cantidad de años de pertenencia al banco: "))
civil = input("¿casado o soltero?: ")
vive = input("¿vive en campo o ciudad?: ")


if anos_banco > 10 and hijos => 2:
  print("aprobado")
elif civil == "casado" and hijos > 3 and 45 =< edad =< 55: 
  print("aprobado")
elif ingreso > 2500000 and civil == "soltero" and vive == "ciudad":
  print("aprobado")
elif ingreso > 3500000 and anos_banco > 5:
  print("aprobado")
elif vive == "campo" and civil == "casado" and hijos < 2:
  print("aprobado")
else :
  print("rechazado")
  