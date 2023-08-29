ingreso=int (input("cual es su ingreso "))
año=int (input("ingrese su año de nacimiento "))
hijos=int (input("cuantos hijos tiene "))
permanencia=int (input("¿cuantos años tiene de permanencia en el banco? "))
estado_civil=str (input("¿cual es su estado civil? c=casado , s= soltero "))
vivencia=str (input("¿vive en campo o cuidad? u=urbano , r=rural "))
edad = 2022-año 
if permanencia>10 and hijos>=2 or estado_civil=="C" and hijos>3 and edad==45 or ingreso>3500000 and permanencia>5 or vivencia=="R" and estado_civil=="C"and hijos<2 :
  print("APROBADO")
else :
 print("REPROBADO")