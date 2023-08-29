#Aprobación de créditos
def evaluar_credito():
  ingreso = float(input("Ingrese su ingreso en pesos: "))
  ano_nacimiento = int(input("Ingrese su año de nacimiento: "))
  num_hijos = int(input("Ingrese el número de hijos: "))
  anos_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
  estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
  ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")
  
  if anos_pertenencia > 10 and num_hijos >= 2:
     return "APROBADO"
  elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - ano_nacimiento) <= 55:
     return "APROBADO"
  elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
     return "APROBADO"
  elif ingreso > 3500000 and anos_pertenencia > 5:
     return "APROBADO"
  elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
     return "APROBADO"
  else:
     return "RECHAZADO"
    
resultado = evaluar_credito()
print("El resultado de la evaluación es:", resultado)