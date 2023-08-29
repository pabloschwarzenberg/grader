#Aprobación de créditos
ingreso = int(input("Ingrese por favor el ingreso que usted tiene(en pesos): "))
anos = int(input("Cuantos años tiene?: "))
hijos = int(input("Cuantos hijos tiene?: "))
pertenencia = int(input("Cuantos años pertenece usted al banco?: "))
estado = str(input("Por favor indique su estado civil (S: soltero; C: casado): "))
vive = str(input("Por favor indique donde vive (U: urbano, R: rural): "))

if anos > 10 and hijos >= 2:
    print("APROBADO")
elif estado == "C" and hijos > 3 and 45 < anos < 55:
    print("APROBADO")
elif ingreso > 2500000 and estado == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vive == "R" and estado == "C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")