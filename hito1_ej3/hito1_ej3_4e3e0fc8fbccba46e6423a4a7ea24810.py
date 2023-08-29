#Aprobación de créditos
ingresos = eval(input(" ingrese sus ingresos en pesos: "))
año_nacimiento = eval(input("ingrese su año de nacimiento: "))
numero_hijos = eval(input("ingrese el numero de hijos: "))
años_pertenencia = eval(input("ingrese su años de pertenencia al banco: "))
estado_civil = input("ingrese su estado civil,soltero:S, casado:C")
donde_vive = input("ingrese el lugar donde vive,U:urbano,R:rural")

edad = año_nacimiento - 2020

if años_pertenencia>10 and numero_hijos>=2:
    print("APROBADO")
elif estado_civil == "C" and numero_hijos>3 and 45<=edad<=55:
    print("APROBADO")
elif ingresos>2500000 and estado_civil == "S" and donde_vive == "C":
    print("APROBADO")
elif ingresos>3500000 and años_pertenencia>5:
    print("APROBADO")
elif donde_vive == "R" and estado_civil == "C" and numero_hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")