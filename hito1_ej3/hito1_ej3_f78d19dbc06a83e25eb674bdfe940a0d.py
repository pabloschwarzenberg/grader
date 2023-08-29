ingreso = float(input("Ingrese su ingreso en pesos: $"))
nacimiento = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese el número de hijos: "))
pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil = input("Ingrese su estado civil ('S' para soltero, 'C' para casado): ")
vive = input("Ingrese 'U' si vive en la ciudad o 'R' si vive en el campo: ")
aprobado = False

if pertenencia > 10 and num_hijos >= 2:
    aprobado = True
elif estado_civil == 'C' and num_hijos > 3 and nacimiento >= 1968 and nacimiento <= 1978:
    aprobado = True
elif ingreso > 2500000 and estado_civil == 'S' and vive == 'U':
    aprobado = True
elif ingreso > 3500000 and pertenencia > 5:
    aprobado = True
elif vive == 'R' and estado_civil == 'C' and num_hijos < 2:
    aprobado = True
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")