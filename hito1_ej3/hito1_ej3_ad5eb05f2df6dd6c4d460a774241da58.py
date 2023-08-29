#Aprobación de créditos
ingreso=int(input("Ingreso (en pesos): "))
nacio=int(input("Año de nacimiento: "))
hijos=int(input("Numero de hijos: "))
pertenece=int(input("Años de pertenencia al banco: "))
estado=input("Estado civil (s:soltero, c:casado): ")
vive=input("Si vive en el campo o ciudad(u:urvano, r:rural): ")

edad=2020-nacio

credito=False

if pertenece>10 and hijos>=2:
    credito=True
elif (estado=="c" or estado=="C") and hijos>3 and (edad>=45 and edad<=55):
    credito=True
elif ingreso>2500000 and (estado=="s" or estado=="S") and (vive=="u" or vive=="U"):
    credito=True
elif ingreso>3500000 and pertenece>5:
    credito=True
elif (vive=="r" or vive=="R") and (estado=="c" or estado=="C") and hijos<2:
    credito=True
if credito==True:
    print("APROBADO")
else:
    print("RECHAZADO")
     