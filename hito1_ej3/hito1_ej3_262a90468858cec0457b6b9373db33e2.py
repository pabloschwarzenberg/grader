Ingresos = eval(input("Ingrese su cantidad de ingresos"))
Nacimiento = eval(input("Ingrese su año de nacimiento"))
Hijos = eval(input("Ingrese cantidad de hijos"))
añosbanco = eval(input("Ingrese su cantidad de años en el banco"))
Estadocivil = input("Ingrese su estado civil (S/C)")
vivienda = input("Ingrese su vivienda (U/R)")
if(añosbanco>=10 and Hijos>=2):
  print("aprobado")
if(Estadocivil == "C" and Hijos>3 and (Nacimiento>=1965 or Nacimiento<=1975)):
  print("aprobado")
if Ingresos>=250000 and Estadocivil== "S" and vivienda == "U":
  print("aprobado")
if(Ingresos >=350000 and añosbanco>5):
   print("aprobado")
if(Hijos>=2 and Estadocivil == "C" and vivienda == "R"):
  print("aprobado")
else:
  print("rechazado")