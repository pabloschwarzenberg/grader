#Aprobación de créditos
ingreso = eval(input("Ingrese un monto en pesos: "))
nacimiento = eval(input("Ingrese su año de nacimiento: "))
n_hijos = eval(input("Ingrese el numero de hijos: "))
pertenece = eval(input("Ingrese los años que ha estado en el banco:"))
estado = input("Ingrese su estado civil (S /C): ")
vive = input("Ingrese donde vive (R o U): ")

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.

if pertenece>10 and n_hijos>=2:
  print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.

elif estado == "C" and n_hijos>3 and (nacimiento - 2020)>=45 or (nacimiento - 2020)<=55 :
  print("APROBADO")

#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.

elif ingreso>2500000 and estado == "S" and vive == "U":
  print("APROBADO")

#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años

elif ingreso>3500000 and pertenece>5:
  print("APROBADO")

#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.

elif vive == "R" and estado == "C" and hijos<2:
  print("APROBADO")

else:
  print("RECHAZADO")