ingreso=int(input("Ingrese monto de su sueldo:"))
nacimiento=int(input("Ingrese año de nacimiento:"))
hijos=int(input("Ingrese numero de hijos:"))
anos=int(input("Ingrese años de pertenencia al banco:"))
civil=input("Ingrese su estado civil: \n S)Soltero \n C)Casado")       
vivienda=input("Ingrese lugar donde vive: \n U)Urbano \n R)Rural")

if anos>10 and hijos>=2:
    print("APROBADO")

elif (civil=="c" or civil=="C") and  hijos>3 and 1961<naciminto<1971:
    print("APROBADO")

elif ingreso>=2500000 and (civil=="s" or civil=="S") and (vivienda=="u" or vivienda=="U"):
    print("APROBADO")

elif ingreso>3500000 and anos>5:
    print("APROBADO")

elif (vivienda=="r" or vivienda=="R") and (civil=="c" or civil=="C") and hijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")        