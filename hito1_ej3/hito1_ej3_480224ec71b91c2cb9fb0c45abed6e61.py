Ingreso=int(input("De cuanto es su ingreso?:"))
Nacimiento=int(input("Ingrese Año de Nacimiento:"))
Hijos=int(input("Cuantos Hijos Posee?:"))
Años_Banco=int(input("Cuantos años pertenece al banco?:"))
Civil=input("Usted es Soltero(S) o casado (C)?:")
Ubicacion=input("Usted vive en el campo (R) o Ciudad (U)?:")
Año=2000
if Años_Banco >=10 and Hijos >=2:
    print("APROBADO")
elif Civil == "C" and Hijos >= 3 and Nacimiento== 1975 or 1965:
    print("APROBADO")
elif Ingreso >=2500000 and Civil =="S" and Ubicacion== "U":
    print("APROBADO")
elif Ingreso >=2500000 and Años_Banco >= 5:
    print("APROBADO")
elif Ubicacion == "R" and Civil == "C" and Hijos <=2:
    print("APROBADO")

else:
    print("RECHAZADO")
