#Aprobación de créditos
pesos= int(input("Ingrese sus ingresos:"))
annio= int(input("Ingrese su año de nacimiento:"))
hijos= int(input("Ingrese su numero de hijos:"))
banco= int(input("Ingrese su años de pertenencia al banco:"))
est= input("Ingrese su estado civil (S: soltero),(C:casado):")
viv= input("Ingrese si vive en Campo(R) o Ciudad(U):")
edad= (2020-annio)
if (((banco>10)and(hijos>=2)) or ((est=="C")and(hijos>3)and(edad==range(45,55))) or ((est=="S")and(viv=="U")and(pesos>2500000)) or ((pesos>3500000)and(banco>5)) or ((viv=="R")and(est=="C")and(hijos<2))):
  print("APROBADO")
else:   
  print("RECHAZADO")     