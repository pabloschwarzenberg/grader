ingresos = int(input("Ingresar Sueldo: "))
edad = int(input("Ingresse edad: "))
cant_hijos = int(input("Ingrese cantidad de hijos: "))
cant_años_banco = int(input("Ingrese Cant. de años perteneciente al banco: "))
estado_civil = input("Ingrese Estado civil (Soltero[S] o Casado)[C]: ")
zona = input("Ingresar zona (RURAL[R] o URBANO[U]: ")
if (cant_años_banco >10 and cant_hijos >= 2):
    print("APROBADO")
elif (estado_civil == "C" and cant_hijos > 3 and edad >= 45 or edad <= 55):
    print("APROBADO")
elif (ingresos >2500000 and estado_civil == "S" and zona == "U"):
    print("APROBADO")
elif(ingresos >3500000 and cant_años_banco >5):
    print("APROBADO")
elif(zona == "R" and estado_civil == "C" and cant_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
