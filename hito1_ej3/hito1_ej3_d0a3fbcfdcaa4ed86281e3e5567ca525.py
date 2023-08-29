# Aprobación de Créditos
# Ingreso de Datos Solicitados

# Ingresos
Ingresos = int(input("Ingrese su sueldo mensual: "))

# Año de nacimiento
Nacimiento = int(input("Ingrese su año de nacimiento: "))

# Cantidad de Hijos
Num_hijos = int(input("ingrese cuantos hijos tiene: "))

# Años como cliente en el banco
Tiempo_en_banco = int(input("Ingrese su tiempo como cliente en el banco: "))

# Estado civil
Estado_civil = input("ingrese su estado civil (S para soltero y C para casado): ")
  
# Tipo de vivienda
Vivienda = input("Ingrese si vive en Ciudad(U) o Campo(R): ")

# Condiciones para la aprovacion del credito
if Tiempo_en_banco > 10 and Num_hijos >= 2:
  print("APROBADO ")
elif Num_hijos > 3 and Nacimiento >= 1977 and Nacimiento <= 1987 and Estado_civil == "C":
  print("APROBADO ")
elif Ingresos > 2500000 and Estado_civil == "S" and Vivienda == "U":
  print("APROBADO ")
elif Ingresos > 3500000 and Tiempo_en_banco > 5:
  print("APROBADO ")
elif Vivienda == "R" and Estado_civil == "C" and Num_hijos < 2:
  print("APROBADO ")
else:
  print("NO APROBADO")