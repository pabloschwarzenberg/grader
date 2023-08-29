#Aprobación de créditos
print(" Para ver si su credito es aprobado ingrese los siguientes datos: ")
ingresos = int(input("sus ingresos : "))
ano_nacimiento = int(input("ingrese su año de nacimiento : "))
n_hijos = int(input("Ingrese su numero de hijos : "))
anos_banco = int(input("Ingrese los años en el banco : "))
print ("Ingrese una C si usted esta casado o una S si esta soltero")
estado_civil = input("estado civil : ")
print("ingrese una U si vive en un lugar urbano o una R si vive en un lugar rural")
residencia = input("lugar de residencia : ")
edad = (2021 - ano_nacimiento)
if (anos_banco >= 10 and n_hijos >= 2):
    print("APROBADO")
elif ( estado_civil == "C" and n_hijos > 3 and edad > 45 and edad < 55):
    print("APROBADO")
elif ( ingresos > 2500000) and (estado_civil == "S") and (residencia == "U"):
    print("APROBADO")
elif ( ingresos > 3500000 ) and ( anos_banco > 5):
    print("APROBADO")
elif ( residencia == "R") and ( estado_civil == "C") and ( n_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")