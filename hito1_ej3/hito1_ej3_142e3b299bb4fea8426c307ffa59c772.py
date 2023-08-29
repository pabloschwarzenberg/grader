#Aprobación de créditos
ingreso=int(input("Ingrese el ingreso del cliente (en pesos): "))
ano_nacimiento=int(input("Ingrese el año de nacimiento del cliente: "))
hijos=int(input("Ingrese el número de hijos del cliente: "))
pertenencia= int(input("Ingrese los años de pertenencia al banco del cliente: "))
estado_civil=input("Ingrese el estado civil del cliente (S para soltero, C para casado): ").upper()
ubicacion=input("Ingrese la ubicación del cliente (U para urbano, R para rural): ").upper()

if (pertenencia>10 and hijos>= 2):
    print("APROBADO")
elif (estado_civil=="C" and hijos>3 and año_nacimiento>=45 and año_nacimiento<=55):
    print("APROBADO")
elif (ingreso>2500000 and estado_civil=="S" and ubicacion=="U"):
    print("APROBADO")
elif (ingreso>3500000 and pertenencia>5):
    print("APROBADO")
elif (ubicacion=="R" and estado_civil=="C" and hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")     