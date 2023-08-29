from datetime import date

today = date.today()
aactual =int(format(today.year))
ingreso =int(input("ingreso"))
ano =int(input("Año de nacimiento"))
nh =int(input("Numero de Hijos"))
apb=int(input("años de pertenencia al banco"))
ec=str(input("S:Soltero, C:casado"))
lugar=input("U: urbano, R: rural")
edad = aactual-ano
if apb>10 and nh>=2:
    print("APROBADO")
if ec=="C" and nh>3 and 45<edad<55:
    print("APROBADO")
if ingreso>2500000 and ec=="S" and lugar =="U":
    print("APROBADO")
if ingreso>3500000 and apb>5:
    print("APROBADO")
if lugar=="R" and ec=="C" and nh<2:
    print("APROBADO")
else:
    print("RECHAZADO")