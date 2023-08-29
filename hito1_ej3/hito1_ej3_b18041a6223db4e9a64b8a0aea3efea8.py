#Aprobación de créditos
S = 1
C = 0
U = 1
R = 0
print("Programa de Aprobación de Creditos")

ingreso = eval(input("Ingreso en pesos: "))
año = eval(input("Ingrese año de nacimiento: "))
hijos = eval(input("Ingrese número de hijos: ")) 
añosbanco = eval(input("Ingrese años de pertenecia al banco: "))
EC = eval(input(" Es soltero o casado S/C: "))
vive = eval(input("Donde vive urbano o rural U/R: "))

if añosbanco > 10 and hijos >= 2:
    print("APROBADO")
if EC == 0 and hijos > 3 and (2020 - año) > 45 and (2020 - año)>=55:
    print("APROBADO")
if ingreso > 2500000 and EC == 1 and vive == 1:
    print("APROBADO")
if ingreso > 3500000 and añosbanco > 5:
    print("APROBADO")
if  vive == 0 and EC == 0 and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")

    