#Aprobación de créditos
ingreso=int(input("ingrese su ingreso en pesos: "))
nacimiento=int(input("ingrese su año de nacimiento: "))
hijos=int(input("ingrese numero de hijos: "))
pertenencia=int(input("ingrese años de pertenencia al banco: "))
estado_civil=input("estado civil S/C S: Soltero, C: Casado: ")
vive=input("campo o ciudad U/R U: Urbano, R: Rural: ")

anos=2022-nacimiento

if pertenencia>10 and hijos>=2:
    print("APROBADO")
elif estado_civil=="C" and hijos>3 and (anos>=45 and anos<=55):
    print("APROBADO")
elif ingreso >= 250000 and estado_civil=="S" and vive=="U":
    print("APROBADO")
elif ingreso >= 350000 and pertenencia> 5:
    print("APROBADO")
elif vive=="R" and estado_civil=="C" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
