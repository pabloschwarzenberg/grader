#Aprobación de créditos #Benjamín araya
ingresosmensuales=int(input("Ingresos mensuales>:$"))
anonacimiento=int(input("Año de nacimiento>:"))
numerohijos=int(input("Número de hijos>:"))
anosbanco=int(input("Años siendo cliente del banco>:"))
estadocivil=input("Estado Civil C(casado)/S(soltero)>:")
vivencia=input("Vives en zona Rural(C)/Urbana(U)>:")
l=2020-anonacimiento
if(anosbanco>10 and numerohijos>=2):
  print("APROBADO")
elif(estadocivil==1 and numerohijos>3 and l>=45 and l<=55):
  print("APROBADO")
elif(ingresosmensuales>2500000 and estadocivil=="S" and vivencia=="U"):
  print("APROBADO")
elif(ingresosmensuales>3500000 and anosbanco>5):
  print("APROBADO")
elif(vivencia=="R" and estadocivil=="C" and numerohijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")