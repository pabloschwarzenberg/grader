#Aprobación de créditos

ingresos=eval(input("ingrese valores"))
nacimiento=eval(input("ingrese su edad"))
hijos=eval(input("ingrese cantidad de hijos"))
tbanco=eval(input("inigrese valor"))
civil=input("ingrese si es (S/C)")
vive=str(input("ingrese dondde vive (R/U)"))



if tbanco>10 and hijos>=2:
  print("APROBADO")
elif civil=="C" and hijos>3 and 45<=(2020-nacimiento)<=55:
  print("APROBADO")
elif ingresos>2500000 and civil=="S" and vive=="U":
  print("APROBADO")
elif ingresos>3500000 and tbanco>5:
  print("APROBADO")
elif vive=="R"and civil=="C" and hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")



