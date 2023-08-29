#Aprobación de créditos
#Entrada
ingreso = int(input("Ingrese el monto de sus ingresos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese si numero de hijos: "))
pertenencia = int(input("Ingrese sus años de pertenecia al banco: "))
e_civil = (input("Ingrese su estado Civil 'S' Soltero 'C' Casado: "))
residencia = (input("Ingrese si vive en la ciudad 'U' o en el campo 'R': "))
edad = 0                 
#Procesamiento
edad = 2021 - nacimiento
if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif (e_civil == 'C' and hijos > 3) and (45 == edad <= 55):
    print("APROBADO")
elif (ingreso > 2500000 and e_civil =='S') and residensia == 'U':
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print ("APROBADO")
elif (residencia == 'R' and e_civil == 'C') and hijos < 2:
    print ("APROBADO")
else:
    print("RECHAZADO")