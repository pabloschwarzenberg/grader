#Aprobación de créditos
ingresos= int(input("ingrese sus ingresos: "))
nacimiento= int(input("ingrese su fecha de nacimiento: "))
hijos= int(input("ingrese su numero de hijos: "))
pertenencia= int(input("ingrese el tiempo de pertenencia al banco: "))
ec= str(input("ingrese estado civil: s para soltero o c para casado: "))
s=1
c=2
hogar= str(input("ingrese si vive en zona urbana o rural:u para zona urbana o r para zona rural: "))
u=3
r=4
print(hogar)
print(ec)
print(hijos)
if(pertenencia>10 and hijos>=2):
  print("APROBADO")
elif(ec==2 and hijos>3 and nacimiento==1975>=1955):
  print("APROBADO")
elif(ingresos>2500000 and ec==1 and hogar==3):
  print("APROBADO")
elif(ingresos>3500000 and pertenencia>5):
  print("APROBADO")
elif(hogar=="R" and ec=="C" and hijos<2):
  print("APROBADO")
else:
  print("RECHAZADO")