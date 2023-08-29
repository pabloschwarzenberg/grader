#Aprobación de créditos
ingresos=int(input("ingreso mensual:"))
nacimiento=int(input("año de nacimiento:"))
hijos=int(input("numero de hijos:"))
pertenencia=int(input("años en el banco:"))
Civil=str(input("estado civil s o c:"))
Lugar=str(input("campo r o ciudad u:"))

edad=2021-nacimiento

if ("pertenencia>10 and hijos>=2"):
    print("APROBADO")
if ("civil== 'a' and hijos>3 and 45<edad<55"): 
    print("APROBADO")
if ("igresos>2500000 and civil=='s' and lugar=='u'"):
    print ("APROBADO")
if ("ingresos>3500000 and pertenencia>5"):
    print("APROBADO")
if ("lugar=="r" and civil=='c' and hijos<2"):
    print("APROBADO")
else:
    print ("RECHAZADO")