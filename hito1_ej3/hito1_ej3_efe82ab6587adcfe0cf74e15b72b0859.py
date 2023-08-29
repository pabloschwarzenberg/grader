#Aprobación de créditos
print("debe ingresar los siguientes datos")
i=eval(input("ingrese sus ingresos:"))
an=eval(input("ingrese su año de nacimiento:"))
nh=eval(input("ingrese su numero de hijos:"))
ab=eval(input("ingrese los años de permanencia en el banco:"))
ec=input("si esta soltero ingrese S y si esta casado C:")
cc=input("si vive en campo ingrese R y si vive en ciudad U:")
f=2020-an
if ab>10 and nh>=2:
  print("aprobado")
elif ec=="C" and nh>3 and 45<=f<=55:
  print("aprobado")
elif i>2500000 and ec=="S" and cc=="U":
  print("aprobado")
elif i>3500000 and ab>5:
  print("aprobado")
elif cc=="R" and ec=="C" and nh<2:
  print("aprobado")
else:
  print("rechazado")