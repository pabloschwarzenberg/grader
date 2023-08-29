ingreso=float(input("ingresos:"))
nacimiento=int(input("año de nacimiento:"))
hijos=int(input("numero de hijos:"))
pertenencia=int(input("años en el banco:"))
civil=input("estado civil:").upper()
vive=input("residencia:").upper()

if pertenencia>11 and hijos>=2:
    print("credito aprobado")

elif  civil== 'c' and  hijos>3  and nacimiento<=1975 and nacimiento>=1965 :
    print("credito aceptado")

elif ingreso>2500000 and civil=='s'and vive=='c':
    print("credito aceptado")

elif ingreso>3500000 and pertenencia>5:
    print("credito aceptado")
elif vive=='c' and civil=='c'and hijos>=2:
    print("credito aceptado")
else:print("credito rechazado")