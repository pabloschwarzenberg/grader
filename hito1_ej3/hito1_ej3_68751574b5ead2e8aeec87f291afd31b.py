Ingresos = int(input("Ingrese sus ingresos totales: "))

Edad = int(input("Ingrese su año de nacimiento: "))

Hijos = int(input("Ingrese cuantos hijos tiene: "))

Banco = int(input("Ingrese cuantos años lleva en el banco: ")

civil = (input("Ingrese su estado civil (S para soltero y C para casado): " ))

vive = (input("Ingrese donde vive (U para urbano y R para rural): "))

if (Banco > 10 and Hijos >= 2):
  print("APROBADO")
  else:
    print("RECHAZADO")
elif (Hijos > 3 and Edad >=1977 and Edad <= 1967 and civil =="C"):
   print("APROBADO")
   else:
     print("RECHAZADO")
elif (Ingresos > 2500000 and civil =="S" and vive == "U"):
  print("APROBADO")
  else:
    print("RECHAZADO")
elif (Ingresos > 3500000 and Banco >= 5):
  print("APROBADO")
  else:
    print("RECHAZADO")
elif (vive == "R" and civil =="C" and Hijos =< 2):
   print("APROBADO")
   else:
      print("RECHAZADO")