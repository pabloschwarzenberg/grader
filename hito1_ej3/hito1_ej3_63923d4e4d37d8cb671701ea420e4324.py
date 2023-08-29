#Aprobación de créditos
Monto_Credito=eval(input("Ingrese Monto de Monto_Credito: "))
Año_Nacimiento=int(input("Ingrese año de Nacimiento: "))
Cant_Hijos=int(input("Ingrese Cantidad de Hijos: "))
Antiguedad=int(input("Ingrese Años de Antiguedad: "))
Estado_civil=input("Ingrese Estado Civil : ")
Residencia=input("Ingrese Ciudad='U:Urbano' o Campo='R: rural : ")
Edad=2021-Año_Nacimiento

if Antiguedad>10 and  Cant_Hijos>=2:
    print("APROBADO")
elif Estado_civil=='C' and Cant_Hijos>3 and Edad>=45 and Edad<=55:
    print("APROBADO")
elif Monto_Credito>2500000 and Estado_civil=='C' and Residencia=='U':
    print("APROBADO")
elif Monto_Credito>3500000 and Antiguedad>5:
    print("APROBADO")
elif Residencia=='R' and Estado_civil=='C' and Cant_Hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
      