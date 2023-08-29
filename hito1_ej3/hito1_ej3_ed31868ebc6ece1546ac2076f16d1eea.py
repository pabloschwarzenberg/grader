#Aprobación de créditos
ingreso=int(input("ingreso: "))
edad=int(input("ingrese su fecha de nacimiento: "))
hijos=int(input("¿cuantos hijos tiene?: "))
permanencia=int(input("ingrese los años de permanencia que tiene en el banco: "))
civil=(input("¿Estado civil?: "))
ur=(input("¿urbano(U) o rural(R): "))

if edad<=1973 and edad<=1963 and hijos<=3:
  print("credito APROBADO")
if permanencia>=10 and hijos>=2:
  print("credito APROBADO")
if ingreso>2500000 and civil=="S" and ur=="U":
    print("credito APROBADO")
if ingreso>3500000 and permanencia>5:
    print("credito APROBADO")
if ur=="R" and civil=="C" and hijos<2:
    print("credito APROBADO")
else:
    print("credito RECHAZADO")

 