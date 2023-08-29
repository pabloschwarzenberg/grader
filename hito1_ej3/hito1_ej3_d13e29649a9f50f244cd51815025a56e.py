#Aprobación de créditos
ingreso = int(input("Ingrese la suma de sus ingresos mensuales:  "))
nacimiento = int(input("Ingrese el año de su nacimiento:  "))
hijos = int(input("Ingrese el numero de hijos que posee:  "))
años_banco = int(input("Ingrese la cantidad de años en el Banco:  "))
estado_civil = (input("Ingrese ,S, si es soltero o ,C, si es casado :  "))
vive = (input("Ingrese ,U, vive en ciudad o ,R, en Campo :  "))

edad = 2022-nacimiento

if años_banco > 10 and hijos >=2 :
    print("APROBADO")
elif estado_civil == "C" and hijos >3 and  55 > edad> 45:
    print("APROBADO") 
elif ingreso>2500000 and estado_civil == "S" and  vive== "U":
     print("APROBADO") 
elif ingreso>3500000 and años_banco >5:    
    print("APROBADO") 
elif vive=="R" and estado_civil == "C" and hijos<2:    
    print("APROBADO") 
else:
    print("RECHAZADO")