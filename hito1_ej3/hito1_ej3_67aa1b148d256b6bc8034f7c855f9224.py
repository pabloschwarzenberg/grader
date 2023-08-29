#entrada 
ingreso = int(input("ingrese su ingreso: "))
año_nac = int(input("ingrese su año de nacimiento: "))
n_hijos = int(input("ingrese su cantidad de hijos: "))
preferencia = int(input("ingrese su años de preferencia del banco: "))
estado = input("ingrese su estado civil C si es casado o S si es soltero: ")
vive = input("ingrese donde vive R para rural o U para urbano: ")

#desarrollo
edad = 2020 - año_nac

#comprobantes
if ((preferencia > 10) and (n_hijos >= 2)):
    print("su credito ha sido APROBADO")
elif ((estado == "C") and (n_hijos > 3) and (edad > 45 and edad < 55)):
    print("su credito ha sido APROBADO")
elif ((ingreso > 2500000) and (estado == "S") and (vive == "U")):
    print("su credito ha sido APROBADO")
elif ((ingreso > 3500000) and (preferencia > 5)):
    print("su credito ha sido APROBADO")
elif ((vive == "R") and (estado == "C") and (n_hijos > 2)):
    print("su credito ha sido APROBADO")
elif ((ingreso > 440000) and (n_hijos > 0) and (estado == "C") and (vive == "R")):
    print("su credito ha sido APROBADO")
else:
    print("su credito ha sido RECHASADO")

