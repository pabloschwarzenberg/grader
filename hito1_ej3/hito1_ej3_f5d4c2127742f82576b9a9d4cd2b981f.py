#Aprobación de créditos
ingreso = int(input("ingrese ingresos: "))
Ano = int(input("ingrese año de nacimiento: "))
nHijos = int(input("ingrese numero de hijos: "))
Abanco = int(input("año de pertenencia al banco: "))
civil = str(input("ingrese estado civil, donde (s) es soltero y (C) es casado: "))
Lugar = str(input("ingrese si vive en lugar urbano o rural, donde (u) es ciudad y (r) es campo:  "))
A = "APROBADO"
R = "RECHAZADO"
edad = (2022-Ano)
if Abanco >= 10 and nHijos >=2:
    print("Su credito es:",A)
elif civil == "C" and nHijos >= 3 and 45<=edad<=55:
    print("Su credito es:", A)
elif ingreso > 2500000 and civil == "S" and Lugar == "U":
    print("Su credito es:", A)
elif ingreso > 3500000 and Abanco > 5:
    print("Su credito es:", A)
elif Lugar == "R" and civil == "C" and nHijos<2:
    print("Su credito es:", A)
else:
    print("Su credito es:", R)