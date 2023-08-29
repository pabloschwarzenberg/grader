#Aprobación de créditosingresos=int(input("Ingresos"))
ingresos=int(input("Ingresos"))
año_de_nacimiento=int(input("Año de nacimiento"))
numero_de_hijos=int(input("Numero de hijos"))
año_de_pertenencia=int(input("Año de pertencia"))
estado_civil=input("Estado civil S para soltero y C para casado")
U_R=input("Vive en campo o ciudad U para urbano y R para rual")
if año_de_pertenencia>10 and numero_de_hijos>=2:
    print("APROBADO")
elif estado_civil=="C" and numero_de_hijos>3 and (año_de_nacimiento>=45 and año_de_nacimiento<=55):
    print("APROBADO")
elif ingresos>2500000 and estado_civil=="S" and U_R=="U":
    print("APROBADO")
elif ingresos>3500000 and año_de_pertenecia>5:
    print("APROBADO")
elif U_R=="R" and estado_civil=="C" and numero_de_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")