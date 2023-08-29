ingreso = int(input("Ingrese su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubicacion = input("Ingrese su ubicación (U para urbano, R para rural): ")

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and hijos > 3 and nacimiento >= 45 and nacimiento <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and ubicacion == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif ubicacion == "R" and estado_civil == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
      