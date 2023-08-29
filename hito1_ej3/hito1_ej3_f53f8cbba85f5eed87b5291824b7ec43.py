ingreso = eval(input("ingreso:\n"))
agno_nacimiento = eval(input("agno de nacimiento:\n"))
cantidad_hijos = eval(input("numero de hijos:\n"))
agno_banco = eval(input("agno de pertencia al banco:\n"))
estado_civil = str(input("(S:soltero, C:casado):\n"))
lugar_residencia = str(input("(U:urbano, R:rural):\n"))

edad = 2020 - agno_nacimiento  

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if(agno_banco >=10 and cantidad_hijos >=2):
  print("APROBADO")  

#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif (estado_civil == ("C")) and (cantidad_hijos > 3) and (45 < edad < 55):
    print("APROBADO")

#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif ingreso > 2500000 and estado_civil=="S" and lugar_residencia=="U":
      print("APROBADO")  
    
#Si el cliente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
# variables ingreso, agno_banco
elif ingreso>3500000 and agno_banco>5:
      print("APROBADO")

#Si el cliente vive en el campo, es casado/a y tiene menos de dos hijos/as.
# variables lugar_residencia, estado_civil, cantidad_hijos
elif lugar_residencia=="R" and estado_civil=="C" and cantidad_hijos < 2:
    print("APROBADO")  

else:
  print('RECHAZADO') 