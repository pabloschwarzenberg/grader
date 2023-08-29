#Aprobación de créditos
ing=int(input("ingrese sus ingresos monetarios :"))
año=int(input("ingrese año de nacimiento"))
hijos=int(input("ingrese el numero de hijos"))
pertenencia=int(input("ingrese años de permanencia"))
estado=input("ingrese estado civil,""(S: soltero, C: casado)""")
ubicacion=input("ingrese la ubicacion de su vivienda,(U: urbano, R: rural)")
año=int(2021-año)
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if(pertenencia>=10 and hijos>=2):
    print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif(estado=="C" and hijos>3 and año>=45 and año<=55):
    print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif(ing>2500000 and estado=="S" and ubicacion=="U"):
    print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif(ing>3500000 and pertenencia>5):
    print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif(ubicacion=="R" and estado=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")