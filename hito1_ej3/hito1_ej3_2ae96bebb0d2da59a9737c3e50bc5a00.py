#Aprobación de créditos
ingreso = int(input())
año = int(input())
hijos = int(input())
años_banco = int(input())
estado = input()
casa = input()
if (años_banco>10) and (hijos>=2):
    print("APROBADO")
elif (estado=="C") and (hijos>3) and (2018-año>=45 and 2018-año<=55):
    print("APROBADO")
elif (ingreso>2500000) and (estado=="S") and (casa=="U"):
    print("APROBADO")
elif (ingreso>3500000) and (años_banco>5):
    print("APROBADO")
elif (casa=="R") and (estado=="C") and (hijos<2):
    print("APROBADO")
else:
    print("NO APROBADO")
