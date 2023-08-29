#Aprobación de créditos
ingreso=int(input("ingrese su ingreso en pesos: "))
ano=int(input("ingrese su año de nacimiento: "))
hijos=int(input("ingrese numero de hijos: "))
banco=int(input("ingrese años de pertenencia al banco: "))
EC=input("ingrese su estado civil (s: soltero, c: casado): ")
vive=input("ingrese en que espacio vive(u: urbano, r: rural)")
if banco>=10 and hijos>=2:
  print("Credito: APROBADO")
elif EC=="c" and hijos>=3 and ano<=55 and 45<=ano:
  print("Credito: APROBADO")  
elif ingreso>=2500000 and EC=="s" and vive=="u":
  print("Credito: APROBADO")
elif ingreso>=3500000 and banco>=5:
  print("Credito: APROBADO")
elif vive=="R" and EC=="C" and hijos<=2:
  print("Credito: APROBADO")
else:
  print("Credito: RECHAZADO")
