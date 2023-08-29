#Aprobación de créditos
ing= int(input("Mencione ingresos: "))
nac= int(input("Ingrese año de nacimiento: "))
hij= int(input("Ingrese número de hijos: "))
per= int(input("Ingrese años de pertenencia al Banco: "))
est= (input("Ingrese Estado Civil, S soltero, C casado: "))
viv= (input("Ingrese si vive en campo R o ciudad U: "))

a= 2022 - nac

if per > 10 and hij >= 2:
  print("APROBADO")
elif est=="C" and hij > 3 and a > 45 and a < 55:
  print("APROBADO")
elif ing > 2500000 and est== "S" and viv== "U":
  print("APROBADO")
elif ing > 3500000 and per > 5:
  print("APROBADO")
elif viv== "R" and est== "C" and hij < 2:
  print("APROBADO")

else:
  print("RECHAZADO")     