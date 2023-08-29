#Aprobación de créditos
print("Aprobación de Créditos")
#Ingresos del cliente
Ingreso=int(input("Digite Ingresos: "))
#Edad del cliente
Año_nacimiento=int(input("Digite Año de Nacimiento: "))
Edad=2021-Año_nacimiento
Número_hijos=int(input("Digite Número de hijos: "))
Años_pertenencia=int(input("Digite Años de pertenencia al banco: "))
Estado_civil=input("Ingrese Estado civil: ")
Hogar=input("Ingrese el lugar donde vive: ")
if Años_pertenencia>10 and Número_hijos>=2:
    print("APROBADO")
elif Estado_civil=="casado" and Número_hijos>3 and 45<=Edad and Edad<55:
 print("APROBADO")
elif Ingreso>2500000 and Estado_civil=="S" and Hogar=="U":
    print("APROBADO")
elif Ingreso>3500000 and Años_pertenencia>5:
    print("APROBADO")
elif Hogar=="R" and Estado_civil=="C" and Número_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")    