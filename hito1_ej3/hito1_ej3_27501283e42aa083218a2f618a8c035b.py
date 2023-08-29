a = float(input( "¿Cuales son sus ingresos anuales?" ))
b= int(input( "ingrese su año de nacimiento" ))
c = int(input( " ¿Cuantos hijos tiene? " ))
d = int(input ( " ¿Hace cuantos años pertenece a este banco? " ))
e=input ( "¿ Usted, es solter@ o casad@? " )
f = input( " ¿ Vive en un lugar urbano o rural? ")
edad = 2021 - b
if   d>10 and c>=2: 
                condicion= "APROBADO " 
elif  e == "C" and c>3 and edad <55 and edad >45 :
                condicion = "APROBADO "
elif e == "S"  and a >2500000 and f == "U" :
              condicion = "APROBADO "
elif a >3500000 and d > 5:
                condicion = "APROBADO " 
elif    f== "R"  and e== "C"  and c<2 :
       condicion = "APROBADO"
else :
       condicion = "RECHAZADO" 
print ( " Desde el banco le informamos que su credito ha sido " , condicion  )    