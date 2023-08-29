#Aprobación de créditos
ingresos= int(input("Ingresos(en pesos): "))
ano_n= int(input("Ingrese año de nacimiento: "))
numero_h= int(input("Ingrese el número de hijos: "))
anos_b= int(input("Años de pertenencia al banco: "))
estado= str(input("S si está soltero, C si está casado: "))
vive= str(input("U si vive en la ciudad, R si vive en el campo: "))

edad= 2018-ano_n

if anos_b>10 and numero_h>=2:
    print("APROBADO")
elif estado=="C" and numero_h>3 and 45<edad<55:
    print("APROBADO")
elif ingresos>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingresos>3500000 and anos_b>5:
    print("APROBADO")
elif vive=="R" and estado=="C" and numero_h<2:
    print("APROBADO")
else:
    print("RECHAZADO")