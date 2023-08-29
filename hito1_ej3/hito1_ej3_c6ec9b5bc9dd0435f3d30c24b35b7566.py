#Aprobación de créditos
ingresos = int(input("Ingrese su cantidad de ingresos: "))
ano_nac = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
anos_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado = input("Ingrese su estado civil: ")
direccion = input("Ingrese donde reside: ")

if anos_banco > 10 and hijos >= 2:
    print("APROBADO")

elif estado == 'C' and hijos > 3 and 1967 < ano > 1977:
    print("APROBADO")

elif ingresos > 2500000 and estado == 'S' and direccion == 'U':
    print("APROBADO")

elif ingresos > 3500000 and anos_banco > 5:
    print("APROBADO")

elif direccion == 'R' and estado == 'C' and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")