#Programa de aplicación de créditos
ingreso=int(input("Ingresa tus ingresos: "))
nacimiento=int(input("Ingresa tu año de nacimiento: "))
hijos=int(input("¿Cuántos hijos tienes?: "))
pertenencia=int(input("Ingrese cantidad de años "))
estado=input("Escribe (S) si estás soltero o (C) si estás casado: ")
vivienda=input("Escribe (R) si vives en el campo o (U) si vives en la ciudad: ")

#Condicionales
if pertenencia >10 and hijos >=2:
    print("APROBADO")
elif estado=="C" and hijos >3 and nacimiento >1967 and nacimiento<1977:
    print("APROBADO")
elif ingreso >=2500000 and estado=="S" and vivienda=="U":
    print("APROBADO")
elif ingreso >=3500000 and pertenencia <5:
    print("APROBADO")
elif vivienda=="R" and estado=="C" and hijos <2:
    print("APROBADO")
else:
    print("RECHAZADO")