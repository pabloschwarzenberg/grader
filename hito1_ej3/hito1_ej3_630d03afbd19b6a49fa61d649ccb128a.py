#Aprobación de créditos
ingreso = eval(input("Ingrese la cantidad de ingresos en pesos: "))        #a = ingresos
anoN = eval(input("Ingrese el año de nacimiento: "))                       #b = año de nacimiento
numeroH = eval(input("Ingrese el numero de hijos: "))                      #c = numero hijos
anosP = eval(input("Ingrese los años de pertenencia al banco: "))          #d = años en el banco
estadoC = input("Ingrese su estado civil (S=Soltero, C=Casado): ")         #e = estado civil
dondeV = input("Ingrese en donde vive (U=Urbano, R=Rural): ")              #f = donde vive

estadoC_str = str(estadoC)
dondeV_str = str(dondeV)

a = estadoC_str[0]
b = dondeV_str[0]

c = 2020 - anoN #los años de la persona

if (anosP > 10) and (numeroH >= 2):
    print("APROBADO")
elif (a == "C") and (numeroH > 3) and (45 <= c <= 55):
    print("APROBADO")
elif (2500000 <= ingreso) and (a == "S") and (b == "U"):
    print("APROBADO")
elif (3500000 <= ingreso) and (5 <= anosP):
    print("APROBADO")
elif (b  == "R") and (a == "C") and (2 > numeroH):
    print("APROBADO")
else:
    print("RECHAZADO")