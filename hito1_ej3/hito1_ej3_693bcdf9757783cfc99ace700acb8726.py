print("========================")
print ("evaliucion de credito")
print("========================")

ingresos= int(input("ingrese su sueldo: "))
nacimiento= int(input("ingrese año de necimiento: "))
hijos= int(input("ingrese numero de hijos: "))
anos= int(input("años de antiguedad en el banco: "))
estado_civil= str(input("ingrese estado civil 'S'si es soltero y 'C' si es casado: "))
lugar= str(input("ingrese lugar donde vive, si es campo 'R' y si es ciudad 'U' : "))
edad=(2021-nacimiento)

if anos > 10 and hijos >= 2 :
    print ("APROBADO")
    
if estado_civil == 'C' and hijos >= 3 and edad >= 45 and edad <= 55 :
    print ("APROBADO")
    
if ingresos > 2500000 and estado_civil == 'S' and lugar == 'U' :
    print ("APROBADO")
    
if ingresos > 3500000 and anos >= 5 :
    print ("APROBADO")
    
if lugar == 'R' and estado_civil == 'C' and hijos < 2 :
    print ("APROBADO")
    
else:
    print("RECHAZADO")




