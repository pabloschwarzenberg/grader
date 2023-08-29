#Aprobación de créditos
ingreso=int(input("cuanto gana usted? $",))
nacimiento=int(input("en que año nacio? ",))
hijos=int(input("cuantos hijos tiene? ",))
pertenencia=int(input("años de pertenencia al banco ",))
estado=str(input("Ingrese su estado civil. 'S' para soltero , 'C' para casado:",))
vivienda=str(input("Ingrese su lugar de vivienda. 'U' para urbano , 'R' para rural:",))
if((pertenencia>10) and (hijos>=2)):
    print("APROBADO")
elif(estado=='C') and (hijos>3) and (1965<=nacimiento<=1975):
    print("APROBADO")
elif(ingreso>2500000) and (estado=='S') and (vivienda=='U'):
    print("APROBADO")
elif(ingreso>3500000) and (pertenencia>5):
    print("APROBADO")
elif(vivienda=='R') and (estado=='C') and (hijos<=2):
    print("APROBADO")
else:
    print("RECHAZADO")