ingresos = int(input("ingrese sus ingresos en pesos : "))
nacimiento = int(input("ingrese su año de nacimiento : "))
hijos = int(input("ingrese numero de hijos "))
antiguedad = int(input("ingrese años de pertenencia al banco : "))
estado = input("intgrese estado civil: ")
vivienda =input("ingrese si vive en campo o ciudad : ")
if estado == "c" :
  c= casado 
elif estado == "s" :
  s=soltero 
  
if vivienda == "r" :
  r=rural 
elif vivienda== "u" :
  u=urbano 
edad = 2020 - nacimiento 

if antiguedad > 10 and hijos >=2:
    print("APROBADO")

elif estado == "c" and hijos >=3 and 45 < edad <55:
    print("APROBADO")

elif ingresos < 2500000 and estado =="s" and vivienda == "u":
    print("APROBADO")

elif ingresos < 3500000 and antiguedad > 5:
    print("APROBADO")

elif vivienda == "r" and estado =="c" and hijos < 2:
    print("APROBADO")

else :
    print("RECHAZADO ")

      