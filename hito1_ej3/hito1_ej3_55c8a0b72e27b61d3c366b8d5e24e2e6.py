#enterada:ingrese ingresos,año de nacimiento, numero de hijos, años quenpertenece al banco,
#estado civil,si vive en campo o ciudad
#salida:muestre si esta aprobado para el credito
#1.ingreso de los datos
ingresos=int(input("ingresos de la persona: "))
while not(ingresos>210000 and ingresos<999999999):
    ingresos=int(input("error, el numero debe ser mayor a 210000 and menor a 999999999: "))
año_de_nacimiento=int(input("año nacimiento: "))
while not(año_de_nacimiento>=1900 and año_de_nacimiento<2021):
    año_de_nacimiento=int(input("el año debe estar entre 1900 y 2020: "))
edad=2020-año_de_nacimiento
numero_hijos=int(input("n de hijos: "))
while not(numero_hijos)>=0:
    numero_hijos=int(input("numero de hijos debe estar entrte 0 y 20:"))
años_pertenencia_banco=int(input("años de pertenencia al banco: "))
while not(años_pertenencia_banco>=0 and años_pertenencia_banco<100):
    años_pertenencia_banco=int(input("los años debe ser mayor o igual a cero y menor que 100: "))
estado_civil=input("estado civil: ")
while not(estado_civil=="S" or estado_civil=="C"):
    estado_civil=input("debe ser S o C: ")
donde_vive=input("campo o ciudad: ")
while not ( donde_vive=="U" or donde_vive=="R"):
    donde_vive=input("la opcion debe ser U(urbano) o R(rural): " )
#verifique si pertenece o no pertenece al banco
if (años_pertenencia_banco>10 and numero_hijos>2):
    print("APROBADO")
elif(estado_civil=="C" and numero_hijos>3 and (edad>=45 and edad<=55)):
    print("APROBADO")
elif(ingresos>2500000 and estado_civil=="S" and donde_vive=="U"):
    print("APROBADO")
elif(ingresos>3500000 and años_pertenencia_banco>5):
    print("APROBADO")
elif(donde_vive=="R" and estado_civil=="C" and numero_hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")
