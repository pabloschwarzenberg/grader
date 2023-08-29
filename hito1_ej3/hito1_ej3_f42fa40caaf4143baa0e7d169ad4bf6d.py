#Aprobación de créditos
ingresos = int(input("Inserte ingresos: "))
nacimiento = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese número de hijos: "))
pertenencia = int(input("Ingrese años de pertenencia al banco: "))
estado = input("Ingrese estado civil (S: soltero / C: casado): ")
vivienda = input("Ingrese donde vive (U: urbano / R: rural): ")
edad = 2022-nacimiento
     
if pertenencia > 10 and hijos>=2:
    print("APROBADO")
elif estado == "C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingresos>2500000 and estado=="S" and vivienda=="U":
    print("APROBADO")
elif ingresos>3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda=="R" and estado=="C" and hijos < 2:
    print("APROBADO")
else:
  print("RECHAZADO")

  
