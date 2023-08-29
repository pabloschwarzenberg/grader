#Aprobación de créditos
ingreso = int(input("ingrese su sueldo: "))
ano_born = int(input("ingrese su año de nacimiento: "))
edad = 2020-ano_born
num_hijos = int(input("ingrese su cantidad de hijos: "))
ano_banco = int(input("ingrese sus años en el banco: "))
estado = str(input("ingrese su estado civil: "))
cc = str(input("ingrese si es urbano o rural "))
if ano_banco>10 and num_hijos>=2:
  print("APROBADO")
elif estado == "C" and num_hijos>3 and edad>=45 and edad<=55:
  print("APROBADO")
elif ingreso>2500000 and estado == "S" and cc == "U":
  print("APROBADO")
elif ingreso>3500000 and ano_banco>5:
  print("APROBADO")
elif cc == "R" and estado == "C" and num_hijos<2:
  print("APROBADO")
else:
  print("RECHAZADO")