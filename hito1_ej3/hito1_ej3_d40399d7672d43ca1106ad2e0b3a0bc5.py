#Aprobación de créditos
#Entradas
ingreso = int(input("Ingrese monto de ingresos:$ "))
nacimiento = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese número de hijos: "))
años_banco = int(input("Ingrese años de pertenencia al banco: "))
e_civil = input("Ingrese Estado Civil, S: Soltero o C: Casado: ")
ubicacion = input("Ingrese ubicación de vivienda, U: Urbano o R: Rural")

#Procesos
if años_banco > 10 and hijos >= 2:
    print("APROBADO")
elif e_civil == "C" and hijos > 3 and 45 >= nacimiento <= 55:
     print("APROBADO")
elif ingreso > 2500000 and e_civil == "S" and ubicacion == "U":
     print("APROBADO")
elif ingreso > 3500000 and años_banco > 5:
     print("APROBADO")
elif ubicacion == "R" and e_civil == "C" and hijos < 2:
     print("APROBADO")
else:  print("RECHAZADO")     