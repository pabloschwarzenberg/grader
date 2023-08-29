#Aprobación de créditos
ingreso=int(input("¿cuantos son sus ingresos?"))

anio=int(input("año de nacimiento"))

numero_de_hijos=int(input("¿cuantos hijos tiene?"))

pertenencia_al_banco=int(input("¿cuantos lleva en este banco?"))

estado_civil= input("¿usted esta S:soltero/a o C:casado/a?")

hogar= input("¿vive en zona R: rural o U:urbana?")

if( pertenencia_al_banco > 10 and numero_de_hijos > 2 ):
    print("APROBADO")


elif( estado_civil == "C" and numero_de_hijos > 3 and 1976<= anio  or anio <= 1966):
     print("APROBADO")

elif( ingreso >= 2500000  and estado_civil == "S" and hogar== "U"):
     print("APROBADO")


elif( ingreso >= 3500000 and  pertenencia_al_banco >5):
    print("APROBADO")


elif( hogar=="R" and estado_civil== "C" and numero_de_hijos < 2):
    print("APROBADO")

else:
    print("RECHAZADO")
      