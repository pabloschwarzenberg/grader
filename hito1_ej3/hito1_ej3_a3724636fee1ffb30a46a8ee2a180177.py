#Aprobación de créditos
print(" Como saber si su credito esta aprobado ")
print(" Complete todos los datos requeridos para saber si es o no apto")
print(" En su estado civil ingrese una C si esta casado o una S si esta soltero")
print(" En su lugar de residencia ingrese U si vive en una urbe o una R si vive en un entorno rural")



I = int(input("sus ingresos : "))
AN = int(input("ingrese su año de nacimiento : "))
H = int(input("numero de hijos : "))
AB = int(input("años en el banco : "))
EC = str(input("estado civil : "))
LR = str(input("lugar de residencia : "))


aos = (2021 - AN)

if (AB >= 10 and H >= 2):
    print("APROBADO")
elif (EC == "C" and H > 3 and aos > 45 and aos < 55):
    print("APROBADO")
elif (I > 2500000) and (EC == "S") and (LR == "U"):
    print("APROBADO")
elif (I > 3500000 ) and (AB> 5):
    print("APROBADO")
elif (LR == "R") and (EC == "C") and (H < 2):
    print("APROBADO")
else:
    print("RECHAZADO")