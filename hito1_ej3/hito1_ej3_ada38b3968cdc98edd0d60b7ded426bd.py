print("Hola Bienvenido")
#Entrada
ingresos = int(input("Cuales son sus Ingresos: "))
año_de_nacimiento = int(input("Año De Nacimiento: "))
numero_hijos = int(input("Cantidad De Hijos: "))
años_banco = int(input("Años De Pertenencia En El Banco: "))
estado_civil = str(input("Estado Civil S Soltero | C Casado: "))
vivienda = str(input("Vive en Ciudad o Campo? U Urbano | R Rural: "))
#Proceso
if años_banco > 10 and numero_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and numero_hijos > 3 and año_de_nacimiento <= 1967 and año_de_nacimiento >= 1977:
    print ("APROBADO")
elif ingresos > 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")
elif ingresos > 3500000 and años_banco > 5:
    print("APROBADO")
elif vivienda == "R" and estado_civil == "C" and numero_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")