ingreso=float(input("Ingreso: $"))
año=int(input("Año de nacimiento: "))
hijos=int(input("Numero de hijos: "))
años_banco=int(input("Años de pertenencia al banco: "))
civil=input("Estado civil (S: soltero, C: casado): ")
cc=input("Ciudad o campo (U: urbano, R: rural): ")
edad= 2016-año

if años_banco>10 and hijos>=2:
    print("APROBADO")
if civil=="C" and hijos>3 and 55<edad<45:
    print("APROBADO")
if ingreso>2500000 and civil=="S" and cc=="U":
    print("APROBADO")
if ingreso>3500000 and años_banco>5:
    print("APROBADO")
if cc=="R" and civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
