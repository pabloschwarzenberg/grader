x1 = int(input("Ingrese su sueldo: "))
x2 = int(input("Ingrese su año de nacimiento: "))
x3 = int(input("Ingrese el numero de sus hijos: "))
x4 = int(input("Ingrese sus años de pertenencia al banco: "))
x5 = (input("Ingrese su estado civil(C o S): "))
x6 = (input("Vive en una zona rural o urabana? (U o R): "))

if x4 > 10 and x3 > 2:
    print('APROBADO')
elif x5 == "C" and x3 > 3 and 55 > x2 and x2 > 45:
    print("APROBADO")
elif x1 > 2500000 and x5 == "S" and x6 == "U":
    print("APROBADO")
elif x1 > 3500000 and x4 > 5:
    print("APROBADO")
elif x6 == "R" and x5 == "C" and x3 < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
