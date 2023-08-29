ingreso=int(input("Ingrese su Ingreso en pesos"))
nacimiento=int(input("Ingrese su Año de nacimiento"))
hijos=int(input("Ingrese su Número de hijos"))
years=int(input("Ingrese sus Años de pertenencia al banco"))
estadocivil=str(input("Estado civil (S: soltero, C: casado)"))
lugar=str(input("U: urbano, R: rural)"))

if years>=10 and hijos>=2:
    print("APROBADO")

elif estadocivil=='C' and hijos>=3 and 1961<=nacimiento<=1971:
    print("APROBADO")

elif ingreso>=2500000 and estadocivil=='S' and lugar=='U':
    print("APROBADO")

elif ingreso>=2500000 and years>=5:
    print("APROBADO")

elif lugar=='R' and estadocivil=='C' and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")