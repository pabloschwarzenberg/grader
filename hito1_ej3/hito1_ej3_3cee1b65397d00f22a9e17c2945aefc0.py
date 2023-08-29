print("ingrese sus ingresos ")
sueldo =int (input())
print("ingrese año de nacimiento")
anoNacimiento =int (input())
edad = 2022-anoNacimiento
print("ingrese su numero de hijos")
hijos = int (input())
print("ingrese años de permanencia en el banco")
anoPermanencia =int (input())
print("ingrese su estado civil (S) o (C) ")
estadoCivil = input()
print ("vive en campo (R) o urbano (U)")
dondeVive = input()
if(anoPermanencia >= 10 and hijos >= 2): 
  print ("APROBADO")
elif estadoCivil=='C' and hijos >=2 and  edad>=45 and edad<55:
  print ("APROBADO")
elif sueldo>2500000 and estadoCivil== 'S' and dondeVive== 'U':
  print ("APROBADO")
elif sueldo>3500000 and anoPermanencia>5:
  print ("APROBADO")
elif dondeVive=='R' and estadoCivil == "C" and hijos<2:
   print ("APROBADO")
else:
  print("RECHAZADO")