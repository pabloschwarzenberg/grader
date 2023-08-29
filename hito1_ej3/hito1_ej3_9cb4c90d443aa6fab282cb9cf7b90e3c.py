#Aprobación de créditos
 
ingreso = int(input("Ingrese su sueldo en pesos: "))
gen = int(input("Ingrese su año de nacimiento: "))
edad = 2020 - gen
numHijos = int(input("Ingrese número de hijos: "))
anioBanco = int(input("Ingrese sus años de pertenencia al banco: "))
estadoC = str(input("Ingrese su estado civil: "))
cOc = str(input("Indique si vive en campo (R) o ciudad (C) "))

if anioBanco>10 and numHijos>=2:
    print("APROBADO")
    
elif estadoC == "C" and numHijos>3 and edad>=45 and edad<=55:
    print("APROBADO")
    
elif ingreso>2500000 and estadoC == "S" and cOc == "U":
    print("APROBADO")
    
elif ingreso>3500000 and anioBanco>5:
    print("APROBADO")
    
elif cOc == "R" and estadoC == "C" and numHijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")