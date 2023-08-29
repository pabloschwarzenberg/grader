#Ingreso (en pesos)
ingreso = int(input("¿cual es su ingreso mensual en pesos?: "))
#Año de nacimiento
fecha_nacimiento =input("¿cual es su fecha de nacimiento?: ")
#Edad
edad = int(input("¿Cual es su edad?: "))              
#Número de hijos
hijos = int(input("¿Cualto hijos tiene? (1,2,3,4): "))             
#Años de pertenencia al banco
antiguedad =int(input("¿Cuantos años de antiguedad tiene en el banco?: "))  
#Estado civil ("S": soltero, "C", casado)
estado_civil = int(input("¿cual es tu estado civil? (1: soltero, 2: casado): "))               
#Si vive en campo o cuidad ("U": urbano, "R": rural)
sector = int(input("¿En que sector vive? (1: urbano, 2: rural): "))
                
# 1era condición
if (antiguedad == ">10 años" or hijos ==">2"):
  print("Su credito esta APROBADO")
else:

  print("Su credito ha sido RECHAZADO")
                
#2da condición
if (estado_civil == "2" or hijos ==">3") and edad >=45<55:
  print("Su credito esta APROBADO")
else:

  print("Su credito ha sido RECHAZADO")

#3era condición
if (ingreso >=2500000 or estado_civil =="1") and sector == 1:
  print("Su credito esta APROBADO")
else:

  print("Su credito ha sido RECHAZADO")  

#4ta condición
if (ingreso >=3500000 or antiguedad ==">10 años") :
  print("Su credito esta APROBADO")
else:

  print("Su credito ha sido RECHAZADO")

#5ta condición
if (estado_civil == 2 or sector == 2) and hijos <=2:
 print("Su credito esta APROBADO")
else:

  print("Su credito ha sido RECHAZADO")   










 