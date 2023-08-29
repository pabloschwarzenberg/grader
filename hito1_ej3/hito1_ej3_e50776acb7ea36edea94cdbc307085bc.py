ingreso=int(input("Ingrese Monto: "))
anio=int(input("Ingrese Año: "))
nhijos=int(input("Ingrese Cantidad de Hijos: "))
anioBanco=int(input("Ingrese Años en el Banco: "))
estado=str(input("Estado Civil S o C: "))
city=str(input("Campo o Ciudad  R o U: "))
a="F"
if anio >10 and nhijos>=2:
    a="T"
elif estado=="C" and nhijos>3 and  45<=anio<=55:
    a="T"
elif estado=="S" and ingreso>2500000 and city=="U":
    a="T"
elif ingreso<3500000 and anioBanco>5:
    a="T"
elif city=="C" and estado=="C" and nhijos<2:
    a="T"
if a=="T":
    print("APROBADO")
else:
    print("RECHAZADO")
