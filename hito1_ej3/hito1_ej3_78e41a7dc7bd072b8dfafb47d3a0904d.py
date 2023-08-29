#Aprobación de créditos
print(" como saber si su credito esta aprobado ")
print(" rellene todos los datos requeridos para saber si es o no apto")
print(" en su estado civil ingrese una C si esta casado o una S si esta soltero")
print(" en su lugar de residencia ingrese U si vive en una urbe o una R si vive en un entorno rural")



i = int(input("sus ingresos : "))
an = int(input("ingrese su año de nacimiento : "))
h = int(input("numero de hijos : "))
ab = int(input("años en el banco : "))
ec = str(input("estado civil : "))
lr = str(input("lugar de residencia : "))


aos = (2021 - an)

if (ab >= 10 and h >= 2):
    print("APROBADO")
elif ( ec == "C" and h > 3 and aos > 45 and aos < 55):
    print("APROBADO")
elif ( i > 2500000) and (ec == "S") and (lr == "U"):
    print("APROBADO")
elif ( i > 3500000 ) and ( ab > 5):
    print("APROBADO")
elif ( lr == "R") and ( ec == "C") and ( h < 2):
    print("APROBADO")
else:
    print("RECHAZADO")