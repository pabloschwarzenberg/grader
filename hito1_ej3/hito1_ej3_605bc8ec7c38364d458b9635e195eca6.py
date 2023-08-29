#Aprobación de créditos
ingresos=int(input("Ingrese un monto: "))
ano_nacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
pertenencia=int(input("Ingrese años de pertencia al banco: "))
estado_civil=str(input("Ingrese estado civil: S soltero o C casado: "))
S=1
C=2
vivienda=str(input("Ingrese si vive en zona rural o urbana: R zona rural o U zona urbana: "))
R=3
U=4
print(vivienda)
print(estado_civil)
print(hijos)
ano=2020
edad=ano-ano_nacimiento
if(pertenencia > 10 and hijos >= 2):
   print("APROBADO")
elif(estado_civil== "C" and hijos > 3 and 45 >= ano-ano_nacimiento <= 55):
   print("APROBADO")
elif(ingresos > 2500000 and estado_civil== "S" and vivienda== "U"):
   print("APROBADO")
elif(ingresos > 3500000 and pertenencia > 5):
   print("APROBADO")
elif(vivienda== "R" and estado_civil== "C" and hijos <= 2):
   print("APROBADO")
else:
   print("RECHAZADO")