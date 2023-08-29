ingreso=int(input("ingreso en pesos: "))
edad=int(input("ingrese su edad de nacimiento: "))
edad1=2023-edad
hijos=int(input("ingrese la cantidad de hijos: "))
años=int(input("años de pertenencia en al banco: "))
estado=input("estado civil S/C : ")
localidad=input("vive en campo o ciudad U/R  : ")
resultado=0
if(años>10 and hijos>=2):
  resultado=1
elif(estado=="C" or estado=="c" and hijos>=3 and edad1<45 and edad1>55):
  resultado=1
elif(ingreso>2500000 and estado=="s" or estado=="S" and localidad=="U"):
  resultado=1
elif(ingreso>3500000 and años>5):
  resultado=1
elif(localidad=="r" or localidad=="R" and estado=="C" or estado=="c" and hijos>=2):
  resultado=1
if(resultado==1):
  print("APROBADO")
elif(resultado==2):
  print("RECHAZADO")