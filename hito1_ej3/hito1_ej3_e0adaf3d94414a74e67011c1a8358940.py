#Aprobación de créditos
ingreso = int(input("Digite sus ingresos en pesos: \n"))
añanc = int(input("¿Cúal es su año de nacimiento? \n"))
numh = int(input("Número de hijos : \n"))
añospb = int(input("Años de pertenencia al banco: \n"))
estadocv = input("Cúal es su estado civil, ingrese S si es soltero o C si es casado: \n")
vive = input("Si vive en el campo ingrese R, Si vive en la ciudad ingrese U: \n")


if añospb >= 10 and numh >= 2:
    print("APROBADO")  
elif estadocv == "C" and numh >= 3 and (añanc >= 1965 and añanc <= 1975):
    print("APROBADO")
elif ingreso >= 2500000 and estadocv == "S" and vive == "R":
        print("APROBADO")
elif ingreso >= 3500000 and añospb >= 5:
    print("APROBADO")
elif  vive == "R" and estadocv == "C" and numh <= 2:
    print("APROBADO")
else:
    print("RECHAZADO")