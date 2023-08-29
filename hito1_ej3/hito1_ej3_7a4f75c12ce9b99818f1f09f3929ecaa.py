#Aprobación de créditos
print("Bienvenido al Banco DaniBanco!")
print("Si quiere contratar nuestros servicios para solicitar su crédito de consumo, por favor ingrese los siguientes datos.")
In = int(input("Ingreso mensual es pesos: "))
An = int(input("Año de nacimiento: "))
Nh = int(input("Número de hijos: "))
Apb = int(input("Años de pertenencia al banco: "))
Ec = input("Para solter@ ingrese S, para casad@ ingrese C: ")
Coc = input("Si vive en el campo ingrese U, si vive en la ciudad ingrese R: ")
edad = 2022 - An

Con1 = (Apb > 10) and (Nh >= 2) 
Con2 = (Ec == "C" and Nh > 3) and (45 < edad < 55)
Con3 = (In > 2500000) and (Ec == "S") and (Coc == "R")
Con4 = (In > 3500000) and (Apb > 5)
Con5 = (Coc == "R") and (Ec == "C") and (Nh < 2)

if Con1 or Con2 or Con3 or Con4 or Con5 == True:
  print("APROBADO")
else:
  print("RECHAZADO")