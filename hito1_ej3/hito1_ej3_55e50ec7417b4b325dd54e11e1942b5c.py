#Aprobación de créditos
ingreso = int(input("¿Cual es su ingreso?"))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cantidad de hijos: "))
pertenencia = int(input("Ingrese cuanto años lleva en el banco: "))
estado = input("Ingrese su estado civil(S: soltero, C: casado): ")
vive = input("Ingrese donde vive(U: urbano, R: rural): ")
edad = 2021 - nacimiento
if pertenencia > 10 and hijos >= 2:
      print("APROBADO")
elif estado == 'C' and hijos > 3 and edad > 45 and edad < 55:
      print("APROBADO")
elif ingreso > 2500000 and estado == 'S' and vive == 'U':
      print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
      print("APROBADO")
elif vive == 'R' and estado == 'C' and hijos < 2:
      print("APROBADO")
else:
      print("RECHAZADO")   