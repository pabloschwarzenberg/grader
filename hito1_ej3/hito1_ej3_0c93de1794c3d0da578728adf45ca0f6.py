#Aprobación de créditos
ingresos = int(input("ingrese sus ingresos: "))
nacimiento = int(input("ingrese el año de nacimiento: "))
hijos = int(input("ingrese cantidad de hijos: "))
año = int(input("ingrese sus años en el banco: "))
estado = input("ingrese estado civil: ")
vive = input("ingrese donde vive: ")
años=2022-año

if(años > 10 and hijos >= 2):
    print("APROBADO")
    
elif(estado == "C" and hijos > 3 and 45 >= años <=55):
    print("APROBADO")
    
elif(ingresos > 2500000 and estado == "S" and vive == "U"):
    print("APROBADO")
    
elif(ingresos > 3500000 and años >  5):
    print("APROBADO")
    
elif(vive == "R" and estado == "C" and hijos < 2):
    print("APROBADO")
    
else:
    print("RECHAZADO")      