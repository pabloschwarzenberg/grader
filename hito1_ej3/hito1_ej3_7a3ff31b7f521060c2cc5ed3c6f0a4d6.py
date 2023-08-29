#Aprobación de créditos
ingreso = int(input("ingrese su ingreso en pesos: "))
año_nac = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese la cantidad de hijos: "))
años_banco = int(input("ingrese sus años en el banco: "))
estado_civil = input("ingrese su estado civil, S:soltero o C:casado:")
dnd_vive = input("ingrese donde vive, U:urbano o R:rural: ")

while True:
    if años_banco>10 and hijos>=2:
        print("APROBADO")
        
    
    elif estado_civil=="S" and hijos>3 and 1967<año_nac<1977:
        print("APROBADO")
        
        
    elif ingreso>2500000 and estado_civil=="S" and dnd_vive=="U":
        print("APROBADO")
        
        
    elif ingreso>3500000 and años_banco>5:
        print("APROBADO")
        
        
    elif dnd_vive=="R" and estado_civil=="C" and hijos<2:
        print("APROBADO")
        
    
    else:
        print("RECHAZADO")
        break