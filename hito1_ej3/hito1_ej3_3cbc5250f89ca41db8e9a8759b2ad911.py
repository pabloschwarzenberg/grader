#APROBACION DE CREDITO PERSONAL
ingreso=int(input("Ingreso(pesos):$"))
ano=int(input("Ingreso ano de nacimiento:"))
hijos=int(input("Numeros de hijos:"))
antiguedad=int(input("Anos de antiguedad en el banco:"))
estado=input("Estado Civil S o C:")
vive=input("Si vive en campo o ciudad (\"U\": urbano, \"R\": rural)")
ano=2021 - ano

estado=estado.lower()
vive=vive.lower()
aprobado="RECHAZADO"

if ano >=10 and hijos >=2:
    aprobado="APROBADO"
if hijos >3 and ano >=45 and ano <=55:
    aprobado="APROBADO"
if ingreso >2500000 and estado=="S" and vive =="u":
    aprobado="APROBADO"
if ingreso >3500000 and antiguedad >5:
    aprobado=="APROBADO"
    
if vive=="r" :
    if estado=="c":
        if hijos<=2:
           aprobado="APROBADO"
if aprobado=="APROBADO":
    print(aprobado)
else:
    print(aprobado)
        
