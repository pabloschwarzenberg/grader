#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso: "))
nacimiento = int(input("Ingreso su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos: "))
pertbanco = int(input("Ingrese los años de pertencia al banco"))
estadocivil = input("¿Cual es su estado civil? S/C: ")
hogar = input("¿En que zon vive? U/R: ")

actual = 2020
edad = actual - nacimiento

if(pertbanco>10 and hijos>=2) or (estadocivil == "C" and hijos>3 and (edad>45 or edad<55)) or (ingreso>2500000 and estadocivil=="S" and hogar=="U") or (ingreso>3500000 and pertbanco>5) or (hogar=="R" and estadocivil=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")