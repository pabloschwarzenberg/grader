#Aprobación de créditos
ingresos=int(input("cual es ss ingresos: "))
nacimiento=int(input("Edad: "))
hijos=int(input("¿Cuantos hijos tiene? :"))
antiguedad=int(input("Años que pertenencia a su banco: "))
estado=input("Soltero=S o Casado=C: ")
vive=input("siudad=S o campo=C: ")
if(antiguedad>10 and hijos>=2):
   print("APROBADO")
elif(estado=="C" and hijos<3 and nacimiento<1978 and nacimiento>1966):
  print("APROBADO")
elif(ingresos>=250000 and estado=="S" and vive=="U"):
  print("APROBADO")
elif(ingresos>=350000 and antiguedad>5):
  print("APROBADO")
elif(vive=="R" and estado=="C" and hijos<2):
  print("APROBADO")

else:
  print("RECHAZADO")