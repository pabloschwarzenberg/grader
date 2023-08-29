Ingreso=eval(input("Ingrese Monto de Ingreso: "))
Año_Nacimiento=int(input("Ingrese año de Nacimiento: "))
Hijos=int(input("Ingrese Cantidad de Hijos: "))
Antiguedad=int(input("Ingrese Años de Antiguedad: "))
Estado_civil=input("Ingrese Estado Civil : ")
Ubicacion_Residencia=input("Ingrese Ciudad='U:Urbano' o Campo='R: rural : ")
Edad=2021-Año_Nacimiento

if Antiguedad>10 and  Hijos>=2:
    print("APROBADO")
elif Estado_civil=='C' and Hijos>3 and Edad>=45 and Edad<=55:
    print("APROBADO")
elif Ingreso>2500000 and Estado_civil=='C' and Ubicacion_Residencia=='U':
    print("APROBADO")
elif Ingreso>3500000 and Antiguedad>5:
    print("APROBADO")
elif Ubicacion_Residencia=='R' and Estado_civil=='C' and Hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
