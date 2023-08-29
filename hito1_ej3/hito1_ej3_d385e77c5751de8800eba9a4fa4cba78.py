#Aprobación de créditos
sueldo=int(input("Ingrese su renta mensual: $"))
nacimiento=int(input("Ingrese el año de nacimiento: "))
n_hijos=int(input("Ingrese el numero de hijos: "))
antiguedad_banco=int(input("¿Cuantos años lleva en el banco?: "))
estado_civil=input("Estado civil (S o C) \n S = soltero \n C = casado) \n:").upper()
residencia=input("Zona donde vive (U o R): \n U = zona urbana \n R = zona rural \n: ").upper()
edad_real = 2021-nacimiento

print("edad_real", edad_real)

credito = ''

if antiguedad_banco>10 and n_hijos>=2:   
    credito = 'APROBADO'
else:
    if estado_civil=="C" and n_hijos>3 and edad_real>=45 and edad_real<=55 :
        credito = 'APROBADO'
    else:
        if sueldo>2500000 and estado_civil=="S" and residencia=="U":
            credito = 'APROBADO'
        else:
            if sueldo>3500000 and antiguedad_banco>5:
                credito = 'APROBADO'
            else:
                if residencia=="R" and estado_civil=="C" and n_hijos<2:
                    credito = 'APROBADO'
                else:
                    credito = 'RECHAZADO'
print(credito)