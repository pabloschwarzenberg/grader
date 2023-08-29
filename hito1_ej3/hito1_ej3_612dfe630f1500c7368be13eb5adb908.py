ingreso=int(input("Ingresos: "))
año_nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("Número de hijos: "))
años_pertenencia=int(input("Años de pertenencia al banco: "))
estado_civil=str(input("Estado civil (S si es soltero, C si es casado): "))
campo_ciudad=str(input("vive en campo o cuidad (U si es urbano, R si es rural): "))
edad=2021-año_nacimiento
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos
if  años_pertenencia>=10 and hijos>=2:
    print("APROBADO ")

#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años
elif estado_civil=="C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")

#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad
elif ingreso<2500000 and estado_civil=="S" and campo_ciudad=="R":
    print("APROBADO")

#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif ingreso<3500000 and años_pertenencia>5:
    print("APROBADO")

#Si el cliente vive en el campo, es casado y tiene menos de dos hijos
elif campo_ciudad==R and estado_civil=="C" and hijos>2:
    ("APROBADO")
else:
    print("REPROBADO")

