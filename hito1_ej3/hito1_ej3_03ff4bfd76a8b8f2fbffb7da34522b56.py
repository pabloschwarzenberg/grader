#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso en pesos: "))
ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese su número de hijos: "))
anos_banco = int(input("Ingrese sus años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S: soltero, C: casado): ")
ubicacion = input("Ingrese su ubicación (U: urbano, R: rural): ")
# Evaluamos las condiciones para decidir si se aprueba o no el crédito
if anos_banco > 10 and num_hijos >= 2:
  print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and ano_nacimiento >= 45 and ano_nacimiento <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and anos_banco > 5:
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
  