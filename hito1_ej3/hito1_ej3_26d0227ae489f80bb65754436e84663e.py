Ingreso=eval(input("Ingreso: "))
Nacimiento=int(input("Ingrese año de nacimiento: "))
Hijos=int(input("Ingrese el numero de hijos: "))
Banco=eval(input("Cantidad de años que ha pertenecido al banco: "))
EstadoCivil=input("Estado Civil: ")
Casa=input("Vive en campo o ciudad: ")
Edad=2020-Nacimiento
Lista=["S", "C", "U", "R"]

if Ingreso>2500000 and EstadoCivil=="S" and Vivienda=="U":
  print("APROBADO")

if EstadoCivil=="C" and Hijos<3 and 45<=Edad<=55:
  print("APROBADO")

if Banco>10 and Hijos>=2:
  print("APROBADO")

if Ingreso>3500000 and Banco>5:
  print("APROBADO")

if Casa=="R" and EstadoCivil=="C" and Hijos<2:
  print("APROBADO")