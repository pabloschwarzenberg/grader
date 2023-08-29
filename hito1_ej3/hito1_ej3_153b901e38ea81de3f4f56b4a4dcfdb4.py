#Aprobación de crédito   
ingreso=int(input("Ingrese su ingreso: "))
ano_nacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese cuantos hijos tiene: "))
anos_banco=int(input("Cuantos años ha estado en el banco?: "))
estado_civil=input("Ingrese su estado civil: ")
urbano_rural=input("Vive en campo o cuidad?: ")
if anos_banco>10 and hijos>=2: 
    print("APROBADO")
elif estado_civil=="C" and hijos>3:
    if ano_nacimiento>1962 and ano_nacimiento<1972:
        print("APROBADO")
elif ingreso>2500000 and estado_civil=="S" and urbano_rural=="U":
    print("APROBADO")
elif ingreso>3500000 and anos_banco>5:
    print("APROBADO")
elif urbano_rural=="R" and estado_civil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")