I=int(input("Ingrese ingresos en pesos:"))
E=2017-int(input("año nacimiento:"))
H=int(input("Ingrese numero de hijos:"))
AB=int(input("¿cuántos años lleva siendo cliente del banco?:"))
EC=input("¿Es usted soltero/a ó casado/a? Ingrese S o C cuando corresponda:")
CC=input("¿Vive en la ciudad o en el banco? Ingrese U o R cuando corresponda:")


if (AB>10) and (H>= 2): 
          print("APROBADO")
elif (EC=="S") and (H>3) and (45>E>55):
          print("APROBADO")
elif (I>2500000) and (EC=="S") and (CC=="U"):
          print("APROBADO")
elif (I>3500000) and (AB>5):
          print("APROBADO")
elif(CC=="R") and (EC=="C") and (2>H):
          print("APROBADO")
else:
          print("RECHAZADO")