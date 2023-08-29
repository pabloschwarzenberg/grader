#Aprobación de créditos
print("Banco")
Ingreso=int(input("Ingreso en pesos: "))
Año=int(input("Año de nacimiento: "))
Actual=int(2022-Año)
Hijos=int(input("Número de hijos: "))
Años=int(input("Años de pertenencia al banco: "))
Civil=input("S:Soltero, C:Casado: ")
Vive=input("U:Vive en ciudad, R:Vive en campo: ")


if Actual>10 and Hijos>1:
    print("APROBADO")
elif Civil=="C" and Hijos>3 and 45<=Actual>=55:
    print("APROBADO")
elif Ingreso>2500000 and Civil=="S" and Vive=="U":
    print("APROBADO")
elif Ingreso>3500000 and Años>5:
    print("APROBADO")
elif Vive=="R" and Civil=="C" and Hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")