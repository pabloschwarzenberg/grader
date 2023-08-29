a = eval(input("Ingresos: "))
s = eval(input("Año de nacimiento: "))
d = eval(input("Numero de hijos: "))
f = eval(input("Año de pertenencia al banco: "))
print("Estado civil")
print("S=Soltero o C=Casado")
z = str(input(":"))
print("Donde vive")
print("U=urbano o R=rural")
x = str(input(":"))
g = ord(z)
h = ord(x)
z= 2020 - s
if(f > 10  and d >= 2):
    print("APROBADO")
else:
    if(g == 67  and d > 3 and  45 > z < 55):
        print("APROBADO")
    else:
        if(a > 2500000 and  g == 83 and h == 3):
            print("APROBADO")
        else:
            if(a > 3500000 and f > 5):
                print("APROBADO")
            else:
                if(h == 82 and g == 67 and d < 2):
                    print("APROBADO")
                else:
                    print("RECHAZADO")
