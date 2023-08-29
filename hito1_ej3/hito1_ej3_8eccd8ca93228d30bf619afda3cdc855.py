#Aprobación de créditos
ingreso = int(input("ingreso total en pesos: " ))
nacimiento = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese numero de hijos :"))
banco = int(input("años de pertenencia en el banco:" ))
print("1.C.\n2.S.\n")
estado = input("elija su estado civil C o S:" )
print("1.U.\n2.R.\n")
vivir = input("elija donde vive U o R:" )
C = 1
S = 2
U = 3
R = 4
edad = 2020 - nacimiento

if banco > 10 and 2 <= hijos:
    print("APROBADO")

elif estado == C and hijos > 3:
    if 45 < edad < 55:
        print("APROBADO")


elif ingreso > 2500000 and estado == S:
    if vivir == U:
        print("APROBADO")
        

elif ingreso > 3500000 and banco > 5:
    print("APROBADO")
    
elif vivir == R and estado == C:
    if 2 > hijos:
        print("APROBADO")
        
else:
    print("RECHAZADO")        