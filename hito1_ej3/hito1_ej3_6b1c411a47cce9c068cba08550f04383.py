#Aprobación de créditos
import datetime
ingreso= float(input("ingrese la cantidad de sus ingresos en pesos: "))    
Y= float(input("ingrese su año de nacimiento: "))
hijos= float(input("ingrese cuantos hijos tiene: "))
x= float(input("ingrese cuantos años lleva en el banco: "))
e= str(input("ingrese su estado civil(S soltero), (C casado): "))
v= str(input("ingrese si vive en campo o cuidad (U: urbano), (R: rural): "))
E= datetime.datetime.now()
m= E.strftime("%m")
edad= (E.year-Y)

if x>10 and hijos>=2:
    print("APROBADO ")
if e=="C" and hijos>3 and edad <=45 and edad <= 55:
    print("APROBADO ")
if ingreso>2500000 and e == "S" and v == "U":
    print("APROBADO ")
if ingreso > 3500000 and x > 5:
    print("APROBADO ")
if v == "R" and e == "C" and hijos < 2:
    print("APROBADO ")
else: 
      print("RECHAZADO")
