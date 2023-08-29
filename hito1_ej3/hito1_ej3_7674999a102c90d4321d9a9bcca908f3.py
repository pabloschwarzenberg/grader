#Aprobación de créditos
ingreso = int(input("ingrese el monto: "))
fecha = int(input("ingrese año de nacimiento: "))
hijos = int(input("ingrese el numero de hijos: "))
años_banco = int(input("ingrese cuanto tiempo pertenece al banco: "))
estado_civil = input("si es soltero S, si es casado C: ")
vivienda = input("si vive en urbano U, rural R: ")
if años_banco > 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "c" and hijos > 3 and (1975 >= fecha >=1965):
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and años_banco > 5:
    print("APROBADO")
elif ingreso > 3500000 and años_banco > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")