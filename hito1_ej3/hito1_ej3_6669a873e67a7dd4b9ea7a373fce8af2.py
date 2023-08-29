#Aprobación de créditos
Ingreso = int(input("ingrese el monto de sus ingresos:"))
Año_de_nacimiento = int(input("ingrese año de nacimiento:"))
edad = Año_de_nacimiento - 2021
Número_de_hijos = int(input("ingrese cantidad de hijos:"))
Años_de_pertenencia_al_banco = int(input("ingrese antiguedad en el banco (en años):"))
Estado_civil =  input("""'S'= soltero , 'C'= casado
ingrese estado civil:""")
lugar_de_residencia = input("""'C'= cuidad , 'R'= rural
ingrese lugar de residencia:""")

if Años_de_pertenencia_al_banco >= 10 and Número_de_hijos >= 2:
    print("APROBADO")
elif Estado_civil == "C" and (edad >= 45 or edad <= 55) and (Número_de_hijos > 3):
    print("APROBADO")
elif Ingreso >= 2500000 and Estado_civil == "S" and lugar_de_residencia == "C":
    print("APROBADO")
elif Ingreso >= 3500000 and Años_de_pertenencia_al_banco >= 5:
    print("APROBADO")
elif lugar_de_residencia == "R" and Estado_civil == "C" and Número_de_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      