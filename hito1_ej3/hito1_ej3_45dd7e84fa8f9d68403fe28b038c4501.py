#Aprobación de créditos
ingreso=int(input("ingrese su sueldo "))
edad=int(input("ingrese su ano nacimiento "))
hijos=int(input("ingrese numero de hijos "))
anos_banco=int(input("ingrese años en el banco "))
estado_civil=(input("estado civil S:soltero C:casado "))
residencia=input("ingrese si vive en el RURAL=R o URBANO=U ")
if anos_banco>10 and hijos>1:
  print("APROBADO")
if estado_civil=="C" and hijos>3 and 2022-edad>46 and 2022-edad<56:
    print("APROBADO")
if ingreso>2500000 and estado_civil=="S" and residencia=="U":
    print("APROBADO")
if ingreso>3500000 and anos_banco>5:
    print("APROBADO")
print("APROBADO") 
if residencia==2 and estado_civil=="C" and hijos<2:
    print("APROBADO")