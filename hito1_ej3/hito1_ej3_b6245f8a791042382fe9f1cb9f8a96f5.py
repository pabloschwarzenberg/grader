ingreso = int(input("cuanto es su ingreso?(en CLP): "))
nacimiento = 2022 - int(input("Ingrese el año de su nacimiento: "))
hijos= int(input("Cuantos hijos tiene?: "))
pertenencia = int(input("Ingrese los años de pertenencia al banco: "))
estado = (input('"S" si es soltero y "C" si es casado": '))
casa = (input('"R" si es rural o "U" si es urbano'))

if pertenencia>10 and hijos>=2:
    print("APROBADO EL CREDITO")
else :
    print ("RECHAZADO EL CREDITO") 
    
if estado == "c" and hijos > 3 and 55>=edad>=45: 
     print("APROBADO EL CREDITO")
else :
    print ("RECHAZADO EL CREDITO")  
    
if ingreso>2500000 and estado == "s" and casa == "u":
     print("APROBADO EL CREDITO")
else :
    print ("RECHAZADO EL CREDITO")
 
if ingreso>3500000 and pertenencia >5:
        print("APROBADO EL CREDITO")
else :
    print ("RECHAZADO EL CREDITO")

if casa == "R" and estado == "C" and hijos < 2:
        print("APROBADO EL CREDITO")