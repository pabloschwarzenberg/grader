#Aprobación de créditos
IN=int(input("numero de ingresos: "))
AN=int(input("año de nacimiento: "))
NH=int(input("numero de hijos: "))
AB=int(input("año pertenencia banco: "))
EC=str(input("S:soltero o C:casado: "))
UR=str(input("U:urbano o R:rural: "))

if(AB>10):
    if(NH>2):
        print("APROBADO")
    else:
        print("RECHAZADO")
if(EC=="C"):
    if(NH>3):
        if(1972>=AN>=1962):
            print("APROBADO")
        else:
            print("RECHAZADO")
    else:
           print("RECHAZADO")
else:
        print("RECHAZADO")
if(IN>2500000) and (EC=="S") and (UR=="U"):
    print ("APROBADO")
else:
    print("RECHAZADO")

if(IN>3500000)and(AB>=5):
    print("APROBADO")
else:
    print("RECHAZADO")
if(UR=="R")and(EC=="C")and(NH<2):
    print("APROBADO")
else:
    print("RECHAZADO")
    
