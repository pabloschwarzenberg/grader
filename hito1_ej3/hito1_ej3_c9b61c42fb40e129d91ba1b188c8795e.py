#Aprobación de créditos
ingreso = int(input("Ingreso en pesos: "))
añoNacimiento = int(input("Año de nacimiento: "))
edad = 2020-añoNacimiento
nroHijos = int(input("Número de hijos: "))
while not (nroHijos>0):
    nroHijos = int(input("Número de hijos: "))
añosPertenencia = int(input("Años de pertenencia al banco: "))
estado = input("Estado civil: ")
residencia = input("Campo o ciudad: ")
if (añosPertenencia>10) and (nroHijos>=2):
    print("APROBADO")
elif (estado == "C") and (nroHijos>3) and (edad>=45 and edad<=55):
    print("APROBADO")
elif (ingreso>2500000) and (estado == "S") and (residencia == "C"):
    print("APROBADO")
elif (ingreso>3500000) and (añosPertenencia>5):
    print("APROBADO")
elif (residencia == "R") and (estado == "C") and (nroHijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")