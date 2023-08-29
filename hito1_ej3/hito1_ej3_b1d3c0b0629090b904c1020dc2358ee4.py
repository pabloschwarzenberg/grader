#Aprobación de créditos
print("Bienvenido a sistema de aprobacion de credito")

ingreso = int(input("Ingrese su ingreso mensual: "))
annos = int(input("Ingrese su fecha nacimiento:"))
hijos = int(input("Ingrese numero de hijos:"))
banco = int(input("Ingrese años de pertenencia en el banco:"))
estado = str(input("Ingrese estado civil: \n(S) Soltero  \n(C) Casado  \n"))
lugar = str(input("Ingrese lugar donde vive: \n(U) Urbano  \n(R) Rural  \n"))

edad = 2020 - annos
if banco > 10 and hijos >= 2 or estado == "S" and hijos > 3 and 45 >= edad <= 55 or ingreso > 2500000 and estado == "S" and lugar == "U"or ingreso > 3500000 and banco > 5 or lugar == "R" and hijos < 2 :  
    print("Credito aprobado")
else :
    print("Credito rechazado")
  