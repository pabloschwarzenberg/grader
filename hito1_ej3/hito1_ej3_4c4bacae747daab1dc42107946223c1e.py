import datetime
pesos=int(input("Digite ingreso (en pesos): "))
año=int(input("Digite año de nacimiento: "))
hijos=int(input("Digite numero de hijos: "))
banco=int(input("Digite años de pertenencia al banco: "))
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
x = datetime.datetime.now()
edad=(x.year)-(año)
while True:
    if banco>10 and hijos>=2:
        print("APROBADO")
        break
    if estadof==1 and hijos>3 and edad>=45 and edad<=55:
        print("APROBADO")
        break
    if pesos>2500000 and estadof==0 and vivef==0:
        print("APROBADO")
        break
    if pesos>3500000 and banco>5:
        print("APROBADO")
        break
    if vivef==1 and estado==1 and hijos<2:
        print("RECHAZADO")
        break
    else:
        print("APROBADO")
        break
