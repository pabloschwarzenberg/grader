#Aprobación de créditos
edad = 0
ingresos = int(input("ingresos: "))
nacimiento = int(input("año nacimiento: "))
if nacimiento >= 2000:
    edad = nacimiento - 2021
if nacimiento < 2000:
    edad = (2000 - nacimiento) + 21
hijos = int(input("cantidad de hijos: "))
permanencia = int(input("años en el banco: "))
estado = input("estado civil (S/C): ")
lugar = input("Urbano o Rural (U/R: ")
print (edad)
if permanencia >= 10 and hijos >= 2:
    print("APROBADO")
elif estado == 'C' and hijos >= 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingresos >= 2500000 and estado == 'S' and lugar == 'U':
    print("APROBADO")
elif ingresos >= 3500000 and permanencia > 5:
    print("APROBADO")
elif lugar == 'R' and hijos < 2 and estado == 'C':
    print("APROBADO")
else:
    print("RECHAZADO")      