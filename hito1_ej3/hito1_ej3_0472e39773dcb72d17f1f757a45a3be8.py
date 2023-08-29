# Entradas

ingresos = int(input("Ingrese sueldo: "))
año = int(input("Ingrese su año de nacimiento: "))
n_hijos = int(input("Ingrese numero de hijos: "))
antiguedad = int(input("Ingrese años de pertenencia al banco: "))
estado_civil = (input("Ingrese su estado civil: "))
vivienda = (input("Ingrese su residencia: "))

# Procesamiento

if antiguedad > 10 and n_hijos >= 2:
    print("APROBADO")

elif estado_civil == "C" and n_hijos >= 3 and edad >= 1965 and edad <= 1975:
    print("APROBADO")

elif ingresos >= 2500000 and estado_civil == "S" and vivienda == "U":
    print("APROBADO")

elif ingresos >= 3500000  and antiguedad > 5:
    print("APROBADO")

elif vivienda == "R" and estado_civil == "C" and n_hijos < 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")

