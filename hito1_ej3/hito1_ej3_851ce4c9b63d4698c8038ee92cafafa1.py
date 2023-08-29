a = eval(input("Ingreso: "))
b = eval(input("Año Nacimiento: "))
c = eval(input("Hijos: "))
d = eval(input("Años de pertenencia al banco: "))
e = input("Estado civil: S(soltero) o C(casado): ")
f = input("Vive en U(urbano) o R(rural): ")

edad = 2020 - b
cond1 = ((d>10) and (c >= 2))
cond2 = ((e == "C") and (c > 3) and (edad >= 45) and (edad <= 55))
cond3 = ((a > 2500000) and (e == "S") and (f == "U"))
cond4 = ((a > 3500000) and (d > 5))
cond5 = ((f == "R") and (e == "C") and (c < 2))

if cond1 == True:
    print("APROBADO")
else:
    if cond2 == True:
        print("APROBADO")
    else:
        if cond3 == True:
            print("APROBADO")
        else:
            if cond4 == True:
                print("APROBADO")
            else:
                if cond5 == True:
                    print("APROBADO")
                else:
                    print("RECHAZADO")