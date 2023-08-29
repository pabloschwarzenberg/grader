#Aprobación de créditos
dinero=int(input("dinero neto mensual sin puntos:"))
fecha_nacimiento=int(input("año de nacimiento:"))
hijos=int(input("cantidad de hijos."))
años_cliente=int(input("años en el banco:"))
estado_civil=str(input("estado civil S = soltero C = casado:"))
domicilio=str(input("U = ciudad R = rural:"))
edad=2021-fecha_nacimiento

if (años_cliente>10 and hijos>=2):
    print("APROBADO")
elif(estado_civil=="C" and hijos > 3 and (edad>45 and edad<55)):
    print("APROBADO")
elif(dinero>2500000 and estado_civil == "S" and domicilio == "U"):
    print("APROBADO")
elif(dinero>3500000 and años_cliente>5):
    print("APROBADO")
elif(domicilio=="R" and estado_civil =="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")