#Aprobación de créditos
##Codigo de aprobacion de credito
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
anos=int(input())
estado=input()
ubicacion=input()
credito= False
if anos>10 and hijos>=2:
    credito = True
if estado== "C" and hijos>=3 and nacimiento>= 1962 and nacimiento <= 1972:
    credito = True
if ingreso> 2500000 and estado== "S" and ubicacion== "U":
    credito = True
if ingreso>3500000 and anos>5:
    credito = True
if ubicacion=="R" and estado== "C" and hijos < 2:
    credito =True
    
if credito:
    print("APROBADO")

else:
    print("RECHAZADO")  