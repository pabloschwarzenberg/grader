#Aprobación de créditos
print("Aprobación de creditos")
print("Para decretar su credito como aprobado ingrese los siguientes datos:")

ingreso=int(input("Ingreso:",))
edad=int(input("Edad:",))
hijos=int(input("Numero de hijos:",))
anos=int(input("Años de pertenencia al banco:",))
estado=(input("Estado civil (S desoltero y C de casado):",))
vivienda=(input("¿Vive en campo o ciudad?(Responder U si vive en ciudad y R si vive en campo):",))

if anos>10 and hijos>=2:
    print("APROBADO")
elif estado=="C" and 45<=edad<=55:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vivienda=="U":
    print("APROBADO")
elif ingreso>3500000 and anos>5:
    print("APROBADO")
elif vivienda=="R" and estado=="C" and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")