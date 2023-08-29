Ingreso=eval(input("Ingrese Monto de Ingreso: "))
Nacimiento=int(input("Ingrese Nacimiento: "))
Cant_Hijos=int(input("Ingrese Cantidad de Cant_Hijos: "))
Antiguedad=int(input("Ingrese Años de Antiguedad: "))
Estado_civil=input("Ingrese Estado Civil : ")
ubicacion_de_residencia=input("Ingrese Ciudad='U:Urbano' o Campo='R: rural : ")
Edad=2021-Nacimiento

if Antiguedad>10 and  Cant_Hijos>=2:
    print("APROBADO")
elif Estado_civil=='C' and Cant_Hijos>3 and Edad>=45 and Edad<=55:
    print("APROBADO")
elif Ingreso>2500000 and Estado_civil=='S' and ubicacion_de_residencia =='U':
    print("APROBADO")
elif Ingreso>3500000 and Antiguedad>5:
    print("APROBADO")
elif ubicacion_de_residencia =='R' and Estado_civil=='C' and Cant_Hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")