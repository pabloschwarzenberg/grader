#Aprobación de créditos
ingreso = eval(input("Escriba sus ingresos en pesos $"))
nacimiento = eval(input("Ingrese su año de nacimiento:"))
hijos = eval(input("Ingrese el numero de hijos:"))
pertenencia = eval(input("Ingrese los años de pertenencia en el banco:"))
estado = input("Estado civil: s = soltero, c = casado: ")
vive = input("Lugar de recidencia: u = urbano, r = rural: ")
edad = 2020 - nacimiento
if (pertenencia >= 10 and hijos >= 2):
    print("APROBADO")
elif (estado == 'C' and hijos > 3 and edad >= 45 and edad <= 55):
    print("APROBADO")
elif (ingreso > 2500000 and estado == 'S' and vive == 'U'):
    print("APROBADO")
elif (ingreso > 3500000 and pertenencia >= 5):
    print("APROBADO")
elif (vive == 'R' and estado == 'C' and hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
