#Aprobación de créditos
Ingreso = int(input("¿Cuál es su Ingreso mensual?"))
Nacimiento = int(input("Indique su año de nacimiento: "))
Hijos = int(input("Ingrese cantidad de hijos: "))
Pertenencia = int(input("Ingrese cuanto años a pertenecido al banco: "))
Estado = input("Ingrese su estado civil(S: soltero, C: casado): ")
Vive = input("Ingrese donde vive(U: urbano, R: rural): ")
Edad = 2021 - Nacimiento
if Pertenencia > 10 and Hijos >= 2:
      print("APROBADO")
elif Estado == 'C' and Hijos > 3 and Edad > 45 and Edad < 55:
      print("APROBADO")
elif Ingreso > 2500000 and Estado == 'S' and Vive == 'U':
      print("APROBADO")
elif Ingreso > 3500000 and Pertenencia > 5:
      print("APROBADO")
elif Vive == 'R' and Estado == 'C' and Hijos < 2:
      print("APROBADO")
else:
      print("RECHAZADO")     