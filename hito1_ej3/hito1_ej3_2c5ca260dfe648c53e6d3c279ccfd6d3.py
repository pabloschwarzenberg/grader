#entrada

#ingresos anuales 
I = float(input( "ingresos anuales :" ))
#fecha de nacimiento 
F= int(input( "ingrese año de nacimiento :" ))
#cantidad de hijos 
H = int(input( " ingrese numero de hijos : " ))
#años de pertenencia en el banco
AP = int(input ( " ingrese años de pertenencia en el banco : " ))
#estado civil
ES=input ( "ingrese estado civil si es  S o C: " )
#campo o ciudad
V = input( " ingrese si vive en un lugar R o U: ")
edad = 2021 - F

#procedimiento
#+10 años 2 o mas hijos
if   AP>10 and H>=2: 
                condicion= "APROBADO "          
# C , + de 3 hijos , edad entre 45 y 55 años 
elif  ES == "C" and H>3 and edad <55 and edad >45 :
                condicion = "APROBADO "
# ingresos superiores a 2500000 , s y vive en r 
elif ES == "S"  and I >2500000 and V == "U" :
              condicion = "APROBADO "           
#ingresos superiores a 3500000 * de 5 años en el banco 
elif I >3500000 and AP > 5:
                condicion = "APROBADO " 
# R , C menos de 2 hijos
elif    V== "R"  and ES== "C"  and H<2 :
                condicion = "APROBADO"
                
else :
                  condicion = "RECHAZADO"

# salida 

print ( " su credito  esta " , condicion  )