print( "bienvenidos a la pagina del banco machintrewe") 
ingreso=int(input("¿cuantos son sus ingresos?"))

an=int(input("año de nacimiento"))

nh=int(input("¿cuantos hijos tiene?"))

apb=int(input("¿cuantos lleva en este banco?"))

ec= input("¿usted esta S:soltero/a o C:casado/a?")

hogar= input("¿vive en zona R: rural o U:urbana?")

if( apb > 10 and nh > 2 ):
    print("APROBADO")
                 

elif( ec == "C" and nh > 3 and 1976<= an  or an <= 1966):
     print("APROBADO")
                 
elif( ingreso >= 2500000  and ec == "S" and hogar== "U"):
     print("APROBADO")
        

elif( ingreso >= 3500000 and  apb >5):
    print("APROBADO")


elif( hogar=="R" and ec== "C" and nh < 2):
    print("APROBADO")

else:
    print("RECHAZADO")  