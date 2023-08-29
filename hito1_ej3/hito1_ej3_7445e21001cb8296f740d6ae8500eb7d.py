#creditos
ingresos = int(input("ingrese cuanto dinero gana en pesos "))
año_nacimiento = int(input("ingrese su año de nacimiento "))
nro_hijos = int(input("ingrese la cantidad de hijos que tiene "))
pertenencia = int(input("ingrese la cantidad de años que lleva perteneciendo al banco "))
estado_civil = str(input("ingrese su estado civil donde S es soltero y C es casado "))
localidad = str(input("ingrese si su localidad es urbana(U) o rural(R) "))
edad = 2022 - año_nacimiento

if edad <= pertenencia:
  print("la edad no puede ser menor o igual al tiempo perteneciendo al banco ")
elif pertenencia >= 10 and nro_hijos >= 2:
  print("APROBADO")
elif estado_civil == "C" and nro_hijos > 3 and edad >= 45 and edad <= 55:
  print("APROBADO")
elif ingresos >= 2500000 and estado_civil == "S" and localidad == "U":
  print("APROBADO")
elif ingresos >= 3500000 and pertenencia >= 5:
  print("APROBADO")
elif localidad == "R" and estado_civil == "C" and nro_hijos <= 2:
  print("APROBADO")
else:
  print("RECHAZADO")