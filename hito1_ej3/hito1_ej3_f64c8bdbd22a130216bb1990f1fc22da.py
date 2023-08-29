#Aprobación de créditos
ingresos = int(input("Ingrese sueldo: "))
año = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el numero de hijos: "))
añosbanco = int(input("Ingrese los años de pertenencia en el banco: "))
estcivil = str(input("Ingrese su estado civil {(S) soltero, (C) casado}: "))
vivienda = str(input("Ingrese si su residencia esta en un campo o en la ciudad {Campo=(R), Ciudad=(U)}: "))
edad = (2020-año)
if(añosbanco>=10 and hijos>=2) or (estcivil=="C" and hijos>3 and 45<=edad<=55) or (ingresos>2500000 and estcivil=="S" and vivienda=="U") or (ingresos>3500000 and añosbanco>5) or (vivienda=="R" and estcivil=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")
      