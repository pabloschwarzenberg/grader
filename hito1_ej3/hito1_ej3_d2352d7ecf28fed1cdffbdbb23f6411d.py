#Aprobación de créditos
ingresos=int(input())
nacimiento=int(input())
hijos=int(input())
banco=int(input())
civil=input()
residencia=input()

edad=int(2017-nacimiento)

if banco>10 and hijos>=2:
    print("APROBADO")
elif civil=="C" and hijos>3 and 45<edad<55:
    print("APROBADO")
elif ingresos>2500000 and civil=="S" and residencia=="U":
    print("APROBADO")
elif ingresos>3500000 and banco>5:
    print("APROBADO")
elif residencia=="R" and civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")