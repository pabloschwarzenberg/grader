#Aprobación de créditos
ingreso=int(input("Ingreso (en pesos): "))
nacimiento=int(input("Ingreso (en pesos): "))
edad= 2022-nacimiento
hijos=int(input("Ingreso (en pesos): "))
abanco=int(input("Ingreso (en pesos): "))
estado_civil=str(input('Ingrese su estado civil "S" si es soltero y "C" si es casado: '))

while estado_civil != "S" or estado_civil!="Soltero" or estado_civil != "C" or estado_civil != "s" or estado_civil != "C" or estado_civil!="Casado":
    estado_civil=str(input("Estado civil incorrecto, ingrese nuevamente: "))

vive=str(input('En donde vive?. Si vive en el campo ingrese "R" rural y si es en la ciudad una "U": '))

while vive != "U" or vive != "R" or vive!="Rural" or vive != "u" or vive!="Urbano" or vive != "r":
    vive=str(input("Opcion incorrecta, ingrese nuevamente: "))

if abanco>10 and hijos>=2:
    print("APROBADO")

elif estado_civil=="C" or estado_civil=="c" or estado_civil=="Casado" and hijos>3 and edad>=45 or edad<=55:
    print("APROBADO")

elif ingreso>2500000 and estado_civil=="S" or estado_civil=="s" or estado_civil=="Soltero":
    print("APROBADO")

elif ingreso>3500000 and abanco>5:
    print("APROBADO")

elif vive=="R" or vive=="r" or vive=="Rural" and estado_civil=="C" or estado_civil=="c" or estado_civil=="Casado" and hijos<2:
    print("APROBADO")