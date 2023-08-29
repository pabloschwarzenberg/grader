#Aprobación de créditos
ingresos=int(input("Ingreso (en pesos):"))
año_de_nacimiento=int(input("Año de nacimiento:"))
cant_de_hijos=int(input("Número de hijos:"))
años_en_el_banco=int(input("Años de pertenencia al banco:"))
estado_civil=input("Estado civil si es soltero o casado (S/C):")
donde_vive=input("Si vive en lo rural o campo (R/C):")
edad= int(2020-año_de_nacimiento)
print(estado_civil)


print("ingresos:", ingresos)
print("año de nacimiento:", año_de_nacimiento)
print("cantidad de hijos:", cant_de_hijos)
print("años en el banco:", años_en_el_banco)
print("estado civil:", estado_civil)
print("donde vive:", donde_vive)

#Datos
C= 0
S= 0.1
R= 0.2
U= 0.3

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos
if(años_en_el_banco>=10) and (cant_de_hijos>=2):
 print("SU CREDITO FUE APROBADO:")

#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años
elif(estado_civil=="C") and (cant_de_hijos>=3)and (edad>=45 and edad<=55):
 print("SU CREDITO FUE APROBADO:")

#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif(ingresos>=2500000)and (estado_civil=="S")and(donde_vive=="U"):
 print("SU CREDITO FUE APROBADO:")

#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif(ingresos>=3500000) and (años_en_el_banco>=5):
 print("SU CREDITO FUE APROBADO:")

#Si el cliente vive en el campo, es casado y tiene menos de dos hijos
elif(donde_vive=="R") and (estado_civil=="C") and (cant_de_hijos<=2):
 print("SU CREDITO FUE APROBADO:")
