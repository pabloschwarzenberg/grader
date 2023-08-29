#Aprobación de créditos
ingreso = int(input("Ingrese los ingresos: "))
year = int(input("Ingrese año de nacimiento: "))
hijos = int(input("Ingrese número de hijos: "))
pertenencia = int(input("Ingrese año de pertenencia: "))
estado = str(input("Ingrese estado civil: "))
lugar = str(input("INgrese lugar de residencia: "))

if pertenencia>10 and hijos>=2:
    print("APROBADO")

elif estado== "C" and hijos>3 and year>=1976 and year<=1966:
    print("APROBADO")

elif ingreso>2500000 and estado == "S" and lugar == "C":
    print("APROBADO")

elif ingreso>3500000 and pertenencia>5:
    print("APROBADO")

elif lugar == "R" and estado == "C" and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")


