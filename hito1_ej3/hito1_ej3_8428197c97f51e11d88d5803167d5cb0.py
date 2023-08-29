#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso mensual en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos que tiene: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
zona_residencia = input("Ingrese zona de residencia (U para urbano, R para rural): ")

# Evaluar las condiciones para aprobación del crédito
if anos_banco > 10 and num_hijos >= 2:
  print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and anio_nacimiento >= 1966 and anio_nacimiento <= 1976:
  print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and zona_residencia == "U":
  print("APROBADO")
elif ingreso > 3500000 and anos_banco > 5:
  print("APROBADO")
elif zona_residencia == "R" and estado_civil == "C" and num_hijos < 2:
  print("APROBADO")
else:
  print("RECHAZADO")      