monto= int(input("ingrese sus ingresos :"))
ano =int (input("ingrese año de nacimiento:"))
hijos=int (input("ingrese numero de hijos:"))
pertenencia= int(input("ingrese años de pertenecia al banco:"))
estado= str(input("estado civil(s:soltero-c:casado)"))
vive=str(input("ingrese si vive en el campo(R) o ciudad(U)"))
ano=2020-ano
if((pertenencia>=10) and (hijos>=2)):
   print("APROBADO")
elif((estado=='C')and(45<=ano<=55)and(hijos>3)):
   print("APROBADO")
elif((monto>250000)and(estado=='S')and(vive=='U')):
   print("APROBADO")
elif((monto>350000)and(pertenencia>5)):
  print("APROBADO")
elif((vive=='R')and(estado=='C')and(hijos<2)):
  print("APROBADO")

else:
  print("rechazado")