#Aprobación de créditos
print("*************Bienvenido al banco Himalaya*************")
print(" ")
print("***Requisitos para aprobar:")
print(" ")
print("***Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.***")
print("***Pertenece más de 10 años al banco, y tiene dos o más hijos***")
print("***Posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad***")
print("***Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años***")
print("***Si el cliente vive en el campo, es casado y tiene menos de dos hijos***")
print(" ")
ingreso=int(input("Digite su Ingreso: "))
a_nac=int(input("Ingrese su año de nacimiento: "))
n_hijos=int(input("Ingrese cantidad de hijos: "))
antiguedad=int(input("Ingrese años de pertenencia en el banco: "))
e_civil=input("Ingrese Estado civil: ")
hogar=input("Ingrese la letra r si vive en campo o la letra u si vive en ciudad: ")
edad=2022-a_nac
if antiguedad > 10 and n_hijos >= 2:
    print("***APROBADO***")   

if e_civil == "c" and n_hijos > 3 and edad > 45 and edad < 55:
    print("***APROBADO***")
if ingreso > 2500000 and e_civil == "s" and hogar == "u":
    print("***APROBADO***")
if ingreso > 3500000 and antiguedad > 5:
    print("***APROBADO***")   
if ingreso > 100000 and hogar == "r" and e_civil == "c" and n_hijos < 2:
    print("***APROBADO***")   
else:
    print("***REPROBADO***")