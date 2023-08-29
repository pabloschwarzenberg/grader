#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
anios_banco = int(input("Ingrese el número de años que lleva en el banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
vive_en = input("Ingrese donde vive (U para urbano, R para rural): ")

# Regla 1
if anios_banco > 10 and num_hijos >= 2:
    print("APROBADO")
# Regla 2
elif estado_civil == "C" and num_hijos > 3 and 45 <= (2023 - anio_nacimiento) <= 55:
    print("APROBADO")
# Regla 3
elif ingreso > 2500000 and estado_civil == "S" and vive_en == "U":
    print("APROBADO")
# Regla 4
elif ingreso > 3500000 and anios_banco > 5:
    print("APROBADO")
# Regla 5
elif estado_civil == "C" and num_hijos < 2 and vive_en == "R":
    print("APROBADO")
else:
    print("RECHAZADO")
