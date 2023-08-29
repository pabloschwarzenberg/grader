Ingreso = int(input("Ingrese sus ingresos en pesos: "))
AñoNac = int(input("Ingrese su año de nacimiento: "))
NumHijos = int(input("Ingrese el número de hijos que tiene: "))
AñosPert = int(input("Ingrese sus años de pertenencia al banco: "))
EstCivil = str(input("Ingrse su estado civil(S:Soltero ; C:Casado): "))
Vive = str(input("Ingrese si vive en campo o ciudad(U:Urbano ; R:Rurual): "))

if AñosPert>10 and NumHijos>=2:
    print("APROBADO")
elif EstCivil =="C" and NumHijos>3 and 45<=(AñoNac - 2020)<=55:
    print("APROBADO")
elif Ingreso > 2500000 and EstCivil =="S" and Vive=="U":
    print("APROBADO")
elif Ingreso>3500000 and AñosPert>5:
    print("APROBADO")
elif Vive=="R" and EstCivil =="C" and NumHijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")