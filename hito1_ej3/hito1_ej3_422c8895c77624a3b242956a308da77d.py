#Aprobación de créditos
def aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion):
  if anios_pertenencia > 10 and num_hijos >= 2:
    return "APROBADO"
  elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    return "APROBADO"
  elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    return "APROBADO"
  elif ingreso > 3500000 and anios_pertenencia > 5:
    return "APROBADO"
  elif ubicacion == "R" and estado_civil == "C" and num_hijos < 2:
    return "APROBADO"
  else:
    return "RECHAZADO"
    
ingreso = int(input("introduzca su ingreso en pesos: ")) 
anio_nacimiento =int(input("ingrese su año de nacimiento: "))
num_hijos =int(input("ingrese el numero de hijos: "))
anios_pertenencia =int(input("ingrese los años de pertenecia al banco: "))
estado_civil =input("ingrese su estado civil (S para soltero, C para casado): ")
ubicacion =input("ingrese su ubicacion (U para urbano, R para rural): ")

decision = aprobar_credito(ingreso, anio_nacimiento, num_hijos, anios_pertenencia, estado_civil, ubicacion)

print(decision)


  
      