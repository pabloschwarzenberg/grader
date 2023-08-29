#Aprobación de créditos
ingreso = int(input( " ingrese sus Ingresos: " ))
nacimiento = int(input( " Ingrese su año de nacimiento: " ))
edad = 2021 - nacimiento
hijos = int(input( " Ingrese el numero de hijos: " )) 
pertenencia = int(input( " Ingrese años de pertenencia al banco: " ))    
civil = input( " ingrese estado civil S (soltero) C (casado): " )
vive = input( " ingrese donde vive U (urbano) R (rural): " )

if pertenencia > 10 and hijos >= 2 :
    print (" el resultado debe ser APROBADO")
elif civil == "C" and hijos > 3 and edad >= 45 and edad <= 55 :
    print (" el resultado debe ser APROBADO " )
elif ingreso > 2500000 and civil == "S" and vive== "U" :
    print ( "el resultado debe ser APROBADO" )
elif ingreso > 3500000 and pertenencia > 5 :
    print ( " el resultado debe ser APROBADO " )
elif vive == "R" and civil == "C" and hijos < 2:
    print ( " el resultado debe ser APROBADO " )

else:
    print ( " el resultado debe ser RECHAZADO " )
    