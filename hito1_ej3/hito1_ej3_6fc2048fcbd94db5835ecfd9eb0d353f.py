#Aprobación de créditos
ingreso=int(input("Ingrese el monto en pesos: "))
nacimiento=int(input("Ingrese el año de nacimiento: "))
hijos=int(input("Ingrese el numero de hijos que tiene:"))
pertenencia= int(input("Ingrese los años de pertenencia al banco:"))
estado=str(input("Ingrese su estado civil S si esta soltero o C si esta casado:"))
vive=str(input("Ingrese una U si vive en espacio urbano o R si vive en espacio rural:"))
edad=2020-nacimiento 

if pertenencia>=10 and hijos>=2:
    print("APROBADO")    
elif estado=="C" and hijos>=3 and 55>edad>45:
    print("APROBADO")
elif ingreso>2500000 and estado=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and pertenencia>=5:
    print("APROBADO")
elif vive=="R" and estado=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")