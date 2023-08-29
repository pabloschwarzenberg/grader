#Aprobación de créditos
#Aprobación de créditos
import datetime
#Los postulantes entregarán al banco la siguiente información:
#Ingreso (en pesos)
pesos=int(input("Digite ingreso (en pesos): "))
#Año de nacimiento
año=int(input("Digite año de nacimiento: "))
#Número de hijos
hijos=int(input("Digite numero de hijos: "))
#Años de pertenencia al banco
banco=int(input("Digite años de pertenencia al banco: "))
#Estado civil ("S": Soltero, "C", Casado)
while True:
    estado=str(input("Introduzca estado civil (Siendo Ss para Soltero y Cc para Casado, según corresponda): "))
    if estado == "s" or estado == "S":
        estadof=0
        break
    elif estado == "c" or estado == "C":
        estadof=1
        break
    else:
        print("Digite correctamente su estado civil.")
        
#Si vive en campo o ciudad("U": Urbano, "R": Rural)
while True:
    vive=input("Introduzca si vive en campo o ciudad (Siendo Uu para Urbano y Rr para Rural, según corresponda): ")
    if vive == "u" or vive == "U":
        vivef=0
        break
    if vive == "r" or vive =="R":
        vivef=1
        break
    else:
        print ("Introduzca correctamente su lugar de residencia.")
#Con una de ellas que se cumpla, se aprueba el crédito:
x = datetime.datetime.now()
edad=(x.year)-(año)
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
while True:
    if banco>10 and hijos>=2:
        print("APROBADO")
        break
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
    if estadof==1 and hijos>3 and edad>=45 and edad<=55:
        print("APROBADO")
        break
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
    if pesos>2500000 and estadof==0 and vivef==0:
        print("APROBADO")
        break
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
    if pesos>3500000 and banco>5:
        print("APROBADO")
        break
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
    if vivef==1 and estado==1 and hijos<2:
        print("RECHAZADO")
        break
    else:
        print("APROBADO")
        break
