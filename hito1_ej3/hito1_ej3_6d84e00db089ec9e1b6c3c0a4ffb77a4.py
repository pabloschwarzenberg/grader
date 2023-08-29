im=int(input("Ingresos mensuales>: $"))
an=int(input("Año de nacimiento>:"))
nh=int(input("Número de hijos>:"))
acb=int(input("Años siendo cliente del banco>:"))
ec=input("Estado Civil C(casado)/S(soltero)>:")
vz=input("Vives en zona Rural(C)/Urbana(U)>:")
e=2020-an
if(acb>10 and nh>=2):
  print("APROBADO")
elif(ec==1 and nh>3 and e>=45 and e<=55):
  print("APROBADO")
elif(im>2500000 and ec=="S" and vz=="U"):
  print("APROBADO")
elif(im>3500000 and acb>5):
  print("APROBADO")
elif(vz=="R" and ec=="C" and nh<2):
  print("APROBADO")
else:
  print("RECHAZADO")
      