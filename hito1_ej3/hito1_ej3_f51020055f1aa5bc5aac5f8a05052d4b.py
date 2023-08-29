#Aprobación de créditos
Ingreso = int(input("indique su Ingreso: "))   
ano = int(input("ingrese el año de nacimiento (ejemplo 1970): "))
hijos = int(input("ingrese cantidad de Hijos: "))
ano_banco = int(input("ingrese años en el Banco: "))
estado_civil = str(input("ingrese estado civil S (soltero)/ C (casado): "))
Zona = str(input("ingrese Zona donde vive U (Urbana) / R (Rural): "))

edad = 2021-ano
Estado="RECHAZADO"      
        
if ano_banco>10 and hijos>=2:
    Estado="APROBADO"      
if estado_civil=="C" and hijos>3 and edad >=45 and edad<=55:
    Estado="APROBADO"
if Ingreso>2500000 and estado_civil=="S" and Zona=="U":
    Estado="APROBADO"
if Ingreso>3500000 and ano_banco>5:
    Estado="APROBADO"
if Zona=="R" and hijos<2:
    Estado="APROBADO"

print(Estado)
