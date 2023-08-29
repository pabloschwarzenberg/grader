#Aprobación de créditos
ingreso=int(input("Introduzca sus ingresos: "))
a=2022-(int(input("Introduzca su año de nacimiento: ")))
h=int(input("Introduza su numero de hijos: "))
ap=int(input("Introduzca sus años de pertenencia en el banco: "))
ec=input("Introduzca su estado civil donde S es soltero y C es casado: ")
v=input("Introduzca su vivienda donde U es Urbano y R es Rural: ")
if ingreso>2500000 and ec== "S" and v=="U" :
 print("APROBADO")
elif ingreso>3500000 and ap>=5 :
 print("APROBADO")
elif ap>=10 and h>2:
 print("APROBADO")
elif ec=="C" and h>=3 and 55<a>45:
 print("APROBADO")
elif v=="R" and ec== "C" and h<2:
 print("APROBADO")
else:
 print ("RECHAZADO")