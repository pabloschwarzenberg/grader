fecha=2017
i=int(input("Ingrese su ingreso mensual:"))
n=int(input("Ingrese su año de nacimiento:"))
h=int(input("Ingrese numero de hijos:"))
a=int(input("Ingrese la cantidad de años que ha estado con nosotros:"))
ec=input("Ingrese su estado civil:")
d=input("Ingrese donde vive:")
if a>10 and h>=2:
 print("APROBADO") 
elif (2017-n>55 and 2017-n<45) and (ec.lower()=="casado" or "c") and h>3:
 print("APROBADO")
elif i>2500000 and (ec.lower()=="soltero" or "s") and (d.lower()=="ciudad" or "c"):
 print("APROBADO")
elif i>3500000 and a>5:
 print("APROBADO")
elif (d.lower()=="rural" or "r") and (ec.lower()=="casado" or "c") and h<=2:
 print("APROBADO")
 
else:
 print("RECHAZADO")