#Aprobación de créditos
a=int(input("Ingrese su ingreso"))
b=int(input("Ingrese su año de nacimiento"))
c=int(input("Ingrese su número de hijos"))
d=int(input("Ingrese su años de pertenencia al banco"))
e=str(input("Ingrese su estado civil"))
f=str(input("Ingrese si vive en campo o ciudad"))
if (d>=10 and c>=2) or ((e=="C") and (c>=3) and (b>= 1965 and b<=1975)) or ((a>=2500000) and (e=="S") and (f=="U")) or ((a>=3500000) and (d>=5)) or ((f=="R") and (e=="C") and (c<=2)):
    print("APROBADO")
else:
    print("Rechazado")
