#Aprobación de créditos
ingreso = int(input("ingrese el ingreso: "))
año_nacimiento = int(input("ingrese su año de nacimiento: "))
numero_hijos = int(input("ingrese el número de hijos: "))
años_pertenecia = int(input("ingrese sus años de pertenencia al banco: "))
estado_civil = input("ingrese su estado civil: (C para CASADO, S para soltero): ")
residencia = input("ingrese su sona de residencia: (U para URBANO) (R para RURAL): ")

if años_pertenecia > 10 and numero_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and numero_hijos > 3 and 45 <= 2023 - año_nacimiento <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and residencia == "U":
    print("APROBADO")
elif ingreso > 3500000 and años_pertenecia > 5:
    print("APBROBADO")
elif residencia == "R" and estado_civil == "C" and numero_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")