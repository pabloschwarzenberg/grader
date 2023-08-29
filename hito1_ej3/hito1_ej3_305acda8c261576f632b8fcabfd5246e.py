#Aprobación de créditos
ingresos=int(input("Ingresos (pesos): "))
ano=int(input("Ingrese su año de nacimiento: "))
nhijos=int(input("Ingrese el numero de hijos que tiene: "))
apb=int(input("Ingrese los años de pertinencia en el banco: "))
estado=str(input("Ingrese su estado civil, Soltero(S) o Casado (C): "))
vive=str(input("Ingrese lugar donde vive, Urbano(U) o Rural (R): "))
edad=(2018)-(ano)


if apb>10 and nhijos>2:
  print("APROBADO")
elif estado=="C" and nhijos>=3 and ano>=45 or ano<=55:
  print("APROBADO")
elif ingresos>2500000 and estado=="S" and vive=="U":
  print("APROBADO")
elif ingresos>3500000 and apb>5:
  print("APROBADO")
elif vive=="R" and estado=="C"and nhijos<2:
  print("APROBADO")
else: 
  print("RECHAZADO")
  


  