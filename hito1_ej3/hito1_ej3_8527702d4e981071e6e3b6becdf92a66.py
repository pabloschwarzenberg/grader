#Aprobación de créditos
x1=int(input("Ingreso(en pesos): "))
x2=int(input("Año de nacimiento: "))
x3=int(input("Numero de hijos: "))
x4=int(input("Años de pertenencia al banco: "))
x5=input("Estado civil: ")
x6=input("Campo o ciudad: ")
if((x4>10)and(x3>2)):
 print("APROBADO")
if((x5=="C")and(x3>3)and(55>(2017-x2)>45)):
 print("APROBADO")
if((x1>2500000)and(x5=="S")and(x6=="U")):
 print("APROBADO")
if((x1>3500000)and(x4>5)):
 print("APROBADO")
if((x6=="R")and(x5=="C")and(x3<2)):
 print("APROBADO")
else:
    print("RECHAZADO")      