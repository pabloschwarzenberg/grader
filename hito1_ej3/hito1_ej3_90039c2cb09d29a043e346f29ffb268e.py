#Aprobación de créditos
ingreso=float(input("ingreso"))
anacimiento=int(input("año nacimiento"))
hijos=int(input("hijos"))
pertbanco=int(input("años pertenencia banco"))
estadocivil=str(input("estado civil"))
campoociudad=str(input("campo o ciudad"))


if pertbanco>10 and hijos>=2:
    print("APROBADO")
elif estadocivil=="C" and hijos>3 and 1963<=anacimiento<=1973:
    print("APROBADO")
elif ingreso>2500000 and estadocivil=="S" and campoociudad=="U":
    print("APROBADO")
elif ingreso>3500000 and pertbanco>5:
    print("APROBADO")
elif campoociudad=="R" and estadocivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
