#Aprobación de créditos
ingresos = int(input())
año_actual = 2017
año_na = int(input())
num_hijos=int(input())
años_pertenencia=int(input())
estado_civil=input()
vivienda=input()
if años_pertenencia >= 10 and num_hijos >=2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos >= 3 and 45 <= (año_actual - año_na) <= 55:
    print("APROBADO")
elif ingresos > 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ingresos > 3500000 and años_pertenencia>5:
    print("APROBADO")
elif vivienda=="R" and estado_civil=="C" and num_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
