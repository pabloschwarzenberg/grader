#Aprobación de créditos
ingresos=int(input("Ingresos:"))
edad=int(input("Edad:"))
hijos=int(input("Número de hijos:"))
years=int(input("Años en el Banco:"))
civil=str(input("Estado civil:"))
live=str(input("Campo o Ciudad:"))


if years>10 and hijos>=2:
    print("APROBADO")
elif civil=="C" and hijos>3 and 45<edad<55:
    print("APROBADO")
elif ingresos>2500000 and civil=="S" and live=="U":
    print("APROBADO")
elif ingresos>3500000 and years>5:
    print("APROBADO")
elif live=="R" and civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
    