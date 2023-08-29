#Aprobación de créditos
ingresos= int(input("ingreso en pesos:$",))
nacimiento= int(input("año de nacimiento:",))
hijos=int(input("cantidad de hijos:",))
añosb= int(input("años de pertenencia al banco:",))
estadocivil= input("estado civil[s(soltero) o c(casado)]:",)
vive= input("donde vive[r(rural) o u(urbano)]:",)
edad= (2020-nacimiento)
s= 1
c= 2
r= 3
u= 4

#aprobacion de credito
if(10<añosb and 2<=hijos):
  print("credito aprobado")
elif(estadocivil==c and 3<=hijos and 45<=edad<=55):
  print("credito aprobado")
elif(ingresos>=2500000 and estadocivil==s and vive==u):
  print("credito aprobado")
elif(ingresos>=3500000 and añosb>5):
  print("credito aprobado")
elif(vive==c and estadocivil==c and hijos<2):
  print("credito aprobado")
else:
  print("credito rechazado")