a = eval(input("ingresos totales: "))
b = eval(input("año de nacimiento: "))
c = eval(input("numero de hijos: "))
d = eval(input("años de pertenencia al banco: "))
e = input("estado civil")
f = input("urbano o rural: ")

if d > 10 and c > 1:
    print("APROBADO")
elif e == "C" and c > 3 and 1965 < b < 1975:
    print("APROBADO")
elif a > 2500000 and e == "S" and f == "U":
    print("APROBADO")
elif a > 3500000 and d > 5:
    print("APROBADO")
elif f == "R" and e == "C" and c < 2:
    print("APROBADO")
else:
    print("REPROBADO")