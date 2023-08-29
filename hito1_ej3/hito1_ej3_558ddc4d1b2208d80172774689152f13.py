#Aprobación de créditos
i = int(input("Ingreso en pesos "))
a = int(input("Ingrese su año de nacimiento "))
n = int(input("Ingrese su numero de hijos "))
p = int(input("Ingrese sus años de pertenencia al banco "))
e = input("Ingrese su estado civil, casado (C) o soltero(S) ")
v = input("Ingrese si vive en el campo (R) o ciudad (U)")

if p > 10 and n >= 2 :
  print("APROBADO")
elif e == "C" and n > 3 and 1968 <= a <= 1978:
  print("APROBADO")
elif i > 2500000 and e == "S" and v == "U":
  print("APROBADO")
elif i > 3500000 and p > 5:
  print("APROBADO")
elif v == "R" and e == "C" and n < 2:
  print("APROBADO")
else:
  print("RECHAZADO")
      