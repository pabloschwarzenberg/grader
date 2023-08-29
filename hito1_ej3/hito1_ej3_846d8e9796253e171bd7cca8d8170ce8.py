ingreso = float(input("Ingrese el ingreso del cliente en pesos: "))
fch_nacimiento = int(input("Ingrese la fecha de nacimiento del cliente: "))
num_hijos = int(input("Ingrese el número de hijos del cliente: "))
fch_pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese el estado civil del cliente (S para soltero, C para casado): ")
lugar_residencia = input("Ingrese el lugar de residencia del cliente (U para urbano, R para rural): ")

aprobado = False

if fch_pertenencia > 10 and num_hijos >= 2:
    aprobado = True
elif estado_civil == "C" and num_hijos > 3 and (fch_nacimiento >= 45 and fch_nacimiento <= 55):
    aprobado = True
elif ingreso > 2500000 and estado_civil == "S" and lugar_residencia == "U":
    aprobado = True
elif ingreso > 3500000 and fch_pertenencia > 5:
    aprobado = True
elif lugar_residencia == "R" and estado_civil == "C" and num_hijos < 2:
    aprobado = True

if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")
