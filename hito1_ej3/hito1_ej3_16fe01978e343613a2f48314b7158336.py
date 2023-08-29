#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso:"))
ano = int(input("Ingrese su año de nacimiento:"))
edad = 2017-ano
hijos = int(input("Cuantos hijos tiene:"))
pertenencia = int(input("Cuantos años lleva perteneciendo a este banco:"))
estado = input("Ingrese su estado civil:")
vivienda = input("Usted vive en el campo en la ciudad:")
if(pertenencia>=10 and hijos>=2):
    print("APROBADO")
    
elif(estado=="C" and hijos>=3 and 45<=edad<=55):
    print("APROBADO")
    
elif(ingreso>=2500000 and estado=="S" and vivienda=="U"):
    print("APROBADO")
    
elif(ingreso>=3500000 and pertenencia>=5):
    print("APROBADO")
elif(estado=="C" and vivienda=="R" and hijos<=2):
    print("APROBADO")
else:
    print("RECHAZADO")
    